class Resource:
    def __init__(self, value, expire):
        self.value = value
        self.expire = expire


class Memcache:
    INT_MAX = 2147483647

    def __init__(self):
        # initialize your data structure here.
        self.cache = {}

    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @return an integer
    def get(self, curtTime, key):
        # Write your code here
        if key not in self.cache:
            return self.INT_MAX
        res = self.cache[key]
        if res.expire == 0 or curtTime <= res.expire:
            return res.value
        return self.INT_MAX

    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @param {int} value an integer
    # @param {int} ttl an integer
    # @return nothing
    def set(self, curtTime, key, value, ttl):
        # Write your code here
        if ttl:
            self.cache[key] = Resource(value, curtTime + ttl - 1)
        else:
            self.cache[key] = Resource(value, 0)

    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @return nothing
    def delete(self, curtTime, key):
        # Write your code here
        if key in self.cache:
            del self.cache[key]

    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @param {int} delta an integer
    # @return an integer
    def incr(self, curtTime, key, delta):
        # Write your code here
        if key not in self.cache:
            return self.INT_MAX
        res = self.cache[key]
        res.value += delta
        return self.get(curtTime, key)

    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @param {int} delta an integer
    # @return an integer
    def decr(self, curtTime, key, delta):
        # Write your code here
        if key not in self.cache:
            return self.INT_MAX
        res = self.cache[key]
        res.value -= delta
        return self.get(curtTime, key)

