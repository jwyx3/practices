# https://leetcode.com/problems/design-hashmap/
# fixed cap, no rehash, simple hashing

class LinkedListNode(object):
    
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None


class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cap = 10007
        self.size = 0
        self.d = [LinkedListNode(0) for _ in xrange(self.cap)]
    
    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        prev = dummy = self.d[key % self.cap]
        curr = dummy.next
        while curr:
            if curr.val[0] == key:
                break
            prev = curr
            curr = curr.next
        if not curr:
            curr = LinkedListNode((key, value))
            curr.prev, prev.next = prev, curr
            self.size += 1
        else:
            curr.val = (key, value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        dummy = self.d[key % self.cap]
        curr = dummy.next
        while curr:
            if curr.val[0] == key:
                break
            curr = curr.next
        return curr.val[1] if curr else -1
        
    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        dummy = self.d[key % self.cap]
        curr = dummy.next
        while curr:
            if curr.val[0] == key:
                break
            curr = curr.next
        if curr:
            curr.prev.next = curr.next
            if curr.next:
                curr.next.prev = curr.prev
            curr.prev = curr.next = None
            self.size -= 1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
