import uuid
import redis
import logging
import time

from flask import Flask, request
from flask_restful import Resource, Api, abort
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.query import LWTException, DoesNotExist

from model import Music, ListenLog, TopkMusic

_LOG = logging.getLogger(__name__)
_NAME = 'topk-music'

_redis_client = None


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
    return _redis_client


def get_app():
    app = Flask(__name__)

    # routing
    api = Api(app)
    api.add_resource(ListenMusic, '/listened')
    api.add_resource(GetTopK, '/topk')

    # create table
    connection.setup(['127.0.0.1'], _NAME, lazy_connect=True,
        retry_connect=True, protocol_version=3)
    sync_table(Music)
    sync_table(ListenLog)
    sync_table(TopkMusic)

    return app

if __name__ == '__main__':
    if not os.getenv('CQLENG_ALLOW_SCHEMA_MANAGEMENT'):
        os.environ['CQLENG_ALLOW_SCHEMA_MANAGEMENT'] = '1'
    app = get_app()
    app.run(debug=True)

