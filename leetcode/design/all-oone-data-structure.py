# https://leetcode.com/problems/all-oone-data-structure/
# key_to_count dict: check key in O(1)
# count_to_bucket dict: get bucket based on count in O(1)
# bucket: double linked list to get max/min
#
# key_to_count and count_to_bucket can be combined into one key_to_bucket.
#

class Bucket(object):
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = self.next = None


class AllOne(object):
    def __init__(self):
        self.key_to_bucket = {}
        self.head = Bucket(0)  # min
        self.tail = Bucket(0)  # max
        self.head.next, self.tail.prev = self.tail, self.head
        self.padding = 0

    def _add_bucket(self, prev, bucket):
        bucket.next, bucket.prev = prev.next, prev
        prev.next = bucket.next.prev = bucket
        return bucket
        
    def _del_bucket(self, curr):
        curr.prev.next, curr.next.prev = curr.next, curr.prev
        
    def _empty(self):
        return self.head.next == self.tail
        
    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        curr = self.head
        if key in self.key_to_bucket:
            curr = self.key_to_bucket[key]
            curr.keys.discard(key)

        count = curr.count + 1
        bucket = curr.next
        if bucket.count != count:
            bucket = self._add_bucket(curr, Bucket(count))
        bucket.keys.add(key)
        self.key_to_bucket[key] = bucket
        
        if curr != self.head and not curr.keys:
            self._del_bucket(curr)
        #self.info()

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.key_to_bucket:
            curr = self.key_to_bucket[key]
            curr.keys.discard(key)
            if curr.count > 1:
                count = curr.count - 1
                bucket = curr.prev
                if bucket.count != count:
                    bucket = self._add_bucket(curr.prev, Bucket(count))
                bucket.keys.add(key)
                self.key_to_bucket[key] = bucket
            elif curr.count == 1:
                del self.key_to_bucket[key]
            if not curr.keys:
                self._del_bucket(curr)
        #self.info()

    def info(self):
        self.padding += 1
        curr = self.head.next
        while curr != self.tail:
            print '>' * self.padding, curr.count, curr.keys
            curr = curr.next
                
    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self._empty():
            return ''
        return next(iter(self.tail.prev.keys))
        
    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self._empty():
            return ''
        return next(iter(self.head.next.keys))
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
