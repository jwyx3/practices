import redis
import logging
import time

from flask import Flask, request
from flask_restful import Resource, Api, abort


_LOG = logging.getLogger(__name__)
_NAME = 'min-project'

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
    return app

if __name__ == '__main__':
    app = get_app()
    app.run(debug=True)

