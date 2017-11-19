import time
import redis
import logging

# incr tinyurl:counter
# sadd into tinyurl:short_id
_ADD_URL_ID = """
local max_id = tonumber(ARGV[1])
local id = redis.call('GET', KEYS[1])
if not id then
   id = 0
else
   id = tonumber(id)
end
if id < max_id then
    local new_id = redis.call('INCR', KEYS[1])
    redis.call('SADD', KEYS[2], new_id)
    return new_id
else
    return max_id
end
"""

_NAME = 'tinyurl'
_MAX_ID = 64 ** 6  # 6 letters of base64
_ADD_THRESHOLD = 500
_COUNTER_KEY = f'{_NAME}:counter'
_AVAILABLE_IDS_KEY = f'{_NAME}:available_ids'
_USED_IDS_KEY = f'{_NAME}:used_ids'

_LOG = logging.getLogger(__name__)

def setup_logger(logger):
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)

setup_logger(_LOG)


def main():
    r = redis.StrictRedis(host='127.0.0.1', port=6379)
    r.script_load(_ADD_URL_ID)
    add_url_id = r.register_script(_ADD_URL_ID)

    while True:
        size = r.scard(_AVAILABLE_IDS_KEY)
        if size < _ADD_THRESHOLD:
            new_id = add_url_id(keys=[_COUNTER_KEY, _AVAILABLE_IDS_KEY], args=[_MAX_ID])
            _LOG.info(f'create url id: {new_id}')
            if int(new_id) == _MAX_ID:
                _LOG.info(f'reach max id {_MAX_ID} and exit')
                break
            time.sleep(0.5)
        else:
            time.sleep(10)

if __name__ == '__main__':
    main()

