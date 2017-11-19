import redis
import logging
import time

from flask import Flask, request
from flask_restful import Resource, Api, abort


_LOG = logging.getLogger(__name__)
_NAME = 'ratelimiter'

_INCR_WITH_EXPIRE = """
local current = redis.call('INCR', KEYS[1])
if tonumber(current) == 1 then
    redis.call('EXPIRE', KEYS[1], tonumber(ARGV[1]))
end
"""

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
        _redis_client.script_load(_INCR_WITH_EXPIRE)
    return _redis_client


class Test1(Resource):
    """ use redis INCR
    2 times per second per user
    """
    def user_limit(self, r, write_pipe, second):
        user = request.environ['HTTP_REMOTE_USER']
        if user:
            incr_with_expire = r.register_script(_INCR_WITH_EXPIRE)
            user_prefix = f'{_NAME}:{user}'
            current = r.get(f'{user_prefix}:{second}')
            current = int(current) if current else 0
            _LOG.info(f'current requests for {user} is: {current}')
            if current and current >= 2:
                abort(429, description=f'Too many requests from {user}.')
            incr_with_expire(keys=[f'{user_prefix}:{second}'], args=[1], client=write_pipe)

    def get(self):
        now = time.time()
        second = int(now)
        r = get_redis_client()
        pipe = r.pipeline()
        self.user_limit(r, pipe, second)
        pipe.execute()
        return {}, 204


class Test2(Resource):
    """ use redis INCR
    2 times per minute per ip
    """
    def addr_limit(self, r, write_pipe, second):
        #import pdb; pdb.set_trace()
        addr = request.environ['HTTP_REMOTE_ADDR']
        if addr:
            incr_with_expire = r.register_script(_INCR_WITH_EXPIRE)
            addr_prefix = f'{_NAME}:{addr}'
            read_pipe = r.pipeline()
            for s in range(second - 59, second + 1):
                read_pipe.get(f'{addr_prefix}:{s}')
            result = read_pipe.execute()
            current = sum(int(x) for x in result if x)
            _LOG.info(f'current requests for {addr} is: {current}')
            if current and current >= 2:
                abort(429, description=f'Too many request from {addr}.')
            incr_with_expire(keys=[f'{addr_prefix}:{second}'], args=[60], client=write_pipe)

    def get(self):
        now = time.time()
        second = int(now)
        r = get_redis_client()
        pipe = r.pipeline()
        self.addr_limit(r, pipe, second)
        pipe.execute()
        return {}, 204


class Test3(Resource):
    """ use redis INCR
    2 times per hour per ip
    """
    def addr_limit(self, r, write_pipe, second, minute):
        #import pdb; pdb.set_trace()
        addr = request.environ['HTTP_REMOTE_ADDR']
        if addr:
            incr_with_expire = r.register_script(_INCR_WITH_EXPIRE)
            addr_prefix = f'{_NAME}:{addr}'
            read_pipe = r.pipeline()
            for s in range(minute * 60, second + 1):
                read_pipe.get(f'{addr_prefix}:{s}')
            for m in range(minute - 59, minute):
                read_pipe.get(f'{addr_prefix}:{m}')
            for s in range((minute - 59) * 60 - 59, (minute - 59) * 60):
                read_pipe.get(f'{addr_prefix}:{s}')
            result = read_pipe.execute()
            current = sum(int(x) for x in result if x)
            _LOG.info(f'current requests for {addr} is: {current}')
            if current and current >= 2:
                abort(429, description=f'Too many request from {addr}.')
            incr_with_expire(keys=[f'{addr_prefix}:{second}'], args=[60], client=write_pipe)
            incr_with_expire(keys=[f'{addr_prefix}:{minute}'], args=[3600], client=write_pipe)

    def get(self):
        now = time.time()
        second = int(now)
        minute = int(now) // 60
        r = get_redis_client()
        pipe = r.pipeline()
        self.addr_limit(r, pipe, second, minute)
        pipe.execute()
        return {}, 204


# TODO: use HSET + in-memory + async update


def get_app():
    app = Flask(__name__)

    # routing
    api = Api(app)
    api.add_resource(Test1, '/test1')
    api.add_resource(Test2, '/test2')
    api.add_resource(Test3, '/test3')

    return app

if __name__ == '__main__':
    app = get_app()
    app.run(debug=True)

