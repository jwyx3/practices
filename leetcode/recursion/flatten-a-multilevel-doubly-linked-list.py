# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
# Time: O(N)
# Space: O(N), stack depth?

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        dummy = Node(0, None, head, None)
        self.helper(dummy)
        return dummy.next

    def helper(self, head):
        tail = node = head
        while node:
            if node.child:
                ctail = self.helper(node.child)
                ctail.next = node.next
                if node.next:
                    node.next.prev = ctail
                node.next = node.child
                node.child.prev = node
                node.child = None
                tail = ctail
                node = ctail.next
            else:
                tail = node
                node = node.next
        return tail
