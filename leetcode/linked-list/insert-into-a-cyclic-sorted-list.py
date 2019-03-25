# https://leetcode.com/problems/insert-into-a-cyclic-sorted-list/
# http://www.cnblogs.com/grandyang/p/9981163.html
# corner case: None, one, duplicate
# Time: O(N)
# Space: O(1)

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution(object):
    def insert(self, head, val):
        """
        :type head: Node
        :type val: int
        :rtype: Node
        """
        if not head:
            node = Node(val)
            node.next = node
            return node
        prev, node = head, Node(val)
        while prev.next != head:
            # prev.val <= prev.next.val
            if prev.val <= val <= prev.next.val:
                break
            # prev.val > prev.next.val
            if prev.val > prev.next.val and (prev.val <= val or prev.next.val >= val):
                break
            prev = prev.next
        node.next, prev.next = prev.next, node
        return head
