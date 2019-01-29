# https://leetcode.com/problems/lfu-cache/
# key_to_node<key, DataNode>
# double linked list: Bucket: count, prev, next, head, tail
# double linked list: DataNode: val, prev, next, bucket
# corner case: capacity == 0

class DataNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None
        self.bucket = None

        
class Bucket(object):
    def __init__(self, count):
        self.count = count
        self.prev = self.next = None
        self.head = DataNode(0, 0)
        self.tail = DataNode(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head
        
    def empty(self):
        return self.head.next == self.tail


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.size = 0
        self.key_to_node = {}
        self.head = Bucket(0)
        self.tail = Bucket(0)
        self.head.next, self.tail.prev = self.tail, self.head

    def _add_node(self, prev, curr):
        curr.next, curr.prev = prev.next, prev
        prev.next = curr.next.prev = curr
        return curr
    
    def _del_node(self, curr):
        curr.prev.next, curr.next.prev = curr.next, curr.prev
        
    def remove_overflow(self):
        node = self.head.next.head.next
        del self.key_to_node[node.key]
        self._del_node(node)
        self.size -= 1
    
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self._del_node(node)
            curr = node.bucket
            count = curr.count + 1
            bucket = curr.next
            if bucket.count != count:
                bucket = self._add_node(curr, Bucket(count))
            self._add_node(bucket.tail.prev, node)
            node.bucket = bucket
            if curr.empty():
                self._del_node(curr)
            #self.info()
            return node.val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.cap == 0:
            return
        
        if key in self.key_to_node:
            node = self.key_to_node[key]
            curr = node.bucket
            count = curr.count + 1
            node.val = value
            self._del_node(node)
        else:
            self.size += 1
            # remove least freq and recently
            if self.size > self.cap:
                self.remove_overflow()
            node = DataNode(key, value)
            self.key_to_node[key] = node
            # insert before tail
            curr, count = self.head, 1

        bucket = curr.next
        if bucket.count != count:
            bucket = self._add_node(curr, Bucket(count))
        node.bucket = bucket
        self._add_node(bucket.tail.prev, node)
        
        if curr != self.head and curr.empty():
            self._del_node(curr)
        #self.info()
            
    def info(self):
        print '---->'
        curr = self.head.next
        while curr != self.tail:
            print '>', curr.count
            dcurr = curr.head.next
            while dcurr != curr.tail:
                print '>>', dcurr.key, dcurr.val
                dcurr = dcurr.next
            curr = curr.next
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
