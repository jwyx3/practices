# idea: space O(n), use hash
# two passes
# 1) create new node
# 2) update next and random

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head: return None
        h, curt = {None: None}, head
        while curt:
            h[curt] = RandomListNode(curt.label)
            curt = curt.next
        curt = head
        while curt:
            h[curt].next = h[curt.next]
            h[curt].random = h[curt.random]
            curt = curt.next
        return h[head]

# TODO: space O(1), use next pointer to save new node
