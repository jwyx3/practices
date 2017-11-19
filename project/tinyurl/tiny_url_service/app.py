import os
import string
import queue
import redis
import logging
from datetime import datetime

from flask import Flask, url_for
from flask_restful import Resource, Api, reqparse, abort
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.query import LWTException, DoesNotExist

from model import Url, CustomUrl


def custom_alias_type(data):
    if 1 <= len(data) <= 32:
        return data
    raise ValueError('The length of custom_alias must be between 1 and 32.')



parser = reqparse.RequestParser()
parser.add_argument('api_key')
parser.add_argument('url', required=True)
parser.add_argument('custom_alias', type=custom_alias_type)
parser.add_argument('expired_at')

_NAME = 'tinyurl'
_AVAILABLE_IDS_KEY = f'{_NAME}:available_ids'
_USED_IDS_KEY = f'{_NAME}:used_ids'
_ID_CACHE_SIZE = 10
_URL_HASH_SIZE = 6
_BASE62_LETTERS = string.digits + string.ascii_letters
_BASE62_REVERSE_MAPPING = {v: i for i, v in enumerate(_BASE62_LETTERS)}

_FETCH_URL_IDS = """
redis.replicate_commands()
local data = redis.call("SPOP", KEYS[1], ARGV[1])
if table.getn(data) > 0 then
    redis.call("SADD", KEYS[2], unpack(data))
    return data
else
    return nil
end
"""

_redis_client = None
_url_ids = queue.Queue()

_LOG = logging.getLogger(__name__)


# helper
def setup_logger(logger):
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)

setup_logger(_LOG)

def get_redis_client():
    global _redis_client
    if not _redis_client:
        _redis_client = r = redis.StrictRedis('127.0.0.1', port=6379)
        r.script_load(_FETCH_URL_IDS)
    return _redis_client


def base62_encode(url_id):
    url_hash_list = []
    while url_id:
        url_hash_list.append(_BASE62_LETTERS[url_id % 62])
        url_id //= 62
    if len(url_hash_list) < _URL_HASH_SIZE:
        url_hash_list = ['0'] * (_URL_HASH_SIZE - len(url_hash_list)) + url_hash_list
    return ''.join(url_hash_list)


def base62_decode(url_hash):
    url_id = 0
    for x in url_hash:
        url_id = url_id * 62 + _BASE62_REVERSE_MAPPING[x]
    return url_id


def get_url_id():
    try:
        url_id = _url_ids.get(timeout=0.1)
    except queue.Empty:
        r = get_redis_client()
        fetch_url_ids = r.register_script(_FETCH_URL_IDS)
        result = fetch_url_ids(keys=[_AVAILABLE_IDS_KEY, _USED_IDS_KEY], args=[_ID_CACHE_SIZE])
        if result:
            for x in result:
                _url_ids.put(int(x))
        url_id = _url_ids.get(timeout=0.1)
    return url_id


class CreateUrl(Resource):
    def post(self):
        args = parser.parse_args()
        if args.get('custom_alias'):
            url_hash = args['custom_alias']
            try:
                CustomUrl.create(
                    id=url_hash, url=args['url'], expired_at=args.get('expired_at'),
                    created_at=datetime.utcnow()
                ).if_not_exists()
            except LWTException:
                pass
        else:
            url_hash = base62_encode(get_url_id())
            _LOG.info(f'use url_hash: {url_hash}')
            Url.create(
                id=url_hash, url=args['url'], expired_at=args.get('expired_at'),
                created_at=datetime.utcnow())
        return {'short_url': url_for('geturl', url_hash=url_hash, _external=True)}, 201


class GetUrl(Resource):
    def get(self, url_hash):
        try:
            url_obj = CustomUrl.get(id=url_hash)
            return {}, 301, {'Location': url_obj['url']}
        except DoesNotExist:
            pass
        try:
            url_obj = Url.get(id=url_hash)
            return {}, 301, {'Location': url_obj['url']}
        except DoesNotExist:
            abort(404, description=f'/{url_hash} is not found')


def get_app():
    app = Flask(__name__)

    # routing
    api = Api(app)
    api.add_resource(CreateUrl, '/shorten')
    api.add_resource(GetUrl, '/<url_hash>')

    # create table
    connection.setup(['127.0.0.1'], _NAME, lazy_connect=True,
        retry_connect=True, protocol_version=3)
    sync_table(Url)
    sync_table(CustomUrl)

    return app

if __name__ == '__main__':
    if not os.getenv('CQLENG_ALLOW_SCHEMA_MANAGEMENT'):
        os.environ['CQLENG_ALLOW_SCHEMA_MANAGEMENT'] = '1'
    app = get_app()
    app.run(debug=True)

