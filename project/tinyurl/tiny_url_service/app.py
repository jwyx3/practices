import datetime
import queue
import grpc

import keygen_pb2
import keygen_pb2_grpc

from flask import Flask, url_for, g
from flask_restful import Resource, Api, reqparse, abort
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table

from model import Url


parser = reqparse.RequestParser()
parser.add_argument('api_key')
parser.add_argument('url', required=True)
parser.add_argument('custom_alias')
parser.add_argument('expired_at')

short_ids = queue.Queue()

# helper
def get_keygen_stub():
    stub = getattr(g, '_keygen_stub', None)
    if stub is None:
        channel = grpc.insecure_channel('localhost:50051')
        stub = g._keygen_stub = keygen_pb2_grpc.KeyGenStub(channel)
    return stub


def get_short_id():
    try:
        short_id = short_ids.get(timeout=0.1)
    except queue.Empty:
        stub = get_keygen_stub()
        keys = stub.GetKeys(keygen_pb2.Empty())
        for key in keys:
            short_ids.put(key.id)
        short_id = short_ids.get(timeout=0.1)
    return short_id


class CreateUrl(Resource):
    def post(self):
        args = parser.parse_args()
        if 'custom_alias' in args:
            short_id = args['custom_alias']
        else:
            short_id = get_short_id()
        url_obj = Url.create(id=short_id, url=args['url'], expired_at=args.get('expired_at'))
        return {'short_url': url_for('geturl', short_id=short_id, _external=True)}, 201


class GetUrl(Resource):
    def get(self, short_id):
        url_objs = Url.objects(id=short_id)
        for url_obj in url_objs:
            return {}, 301, {'Location': cassandra[url_obj.id]['url']}
        abort(404, description=f'/{short_id} is not found')


def get_app():
    app = Flask(__name__)

    # routing
    api = Api(app)
    api.add_resource(CreateUrl, '/shorten')
    api.add_resource(GetUrl, '/<short_id>')

    # create table
    connection.setup(['127.0.0.1'], "tinyurl", lazy_connect=True,
        retry_connect=True, protocol_version=3)
    sync_table(Url)

    return app

if __name__ == '__main__':
    app = get_app()
    app.run(debug=True)

