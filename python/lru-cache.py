# single linked list
# save previous node in hash
class LinkedNode(object):
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        # write your code here
        self.capacity = capacity
        self.h = {}
        self.head = LinkedNode(0, 0)
        self.tail = self.head

    def push_back(self, node):
        # update prev as current tail
        self.h[node.key] = self.tail
        # append this node to tail
        self.tail.next = node
        # update tail pointer
        self.tail = node

    def pop_front(self):
        del self.h[self.head.next.key]
        self.head.next = self.head.next.next
        self.h[self.head.next.key] = self.head

    # move node to tail and update prev of this node
    def kick(self, prev):
        node = prev.next
        # If it's tail now, do nothing
        if node == self.tail:
            return
        # remove node from original position
        prev.next = node.next
        # update prev of original next node
        # set next of moving node to None
        if node.next is not None:
            self.h[node.next.key] = prev
            node.next = None
        self.push_back(node)

    # @return an integer
    def get(self, key):
        # write your code here
        if key not in self.h:
            return -1
        # move node to tail and update prev in h
        self.kick(self.h[key])
        # read val using new prev
        return self.h[key].next.val


    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        # write your code here
        if key in self.h:
            self.kick(self.h[key])
            self.h[key].next.val = value
        else:
            self.push_back(LinkedNode(key, value))
            if len(self.h) > self.capacity:
                self.pop_front()


# TODO: double linked list
