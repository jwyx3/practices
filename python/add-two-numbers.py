# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2
    def addLists(self, l1, l2):
        d1 = h1 = ListNode(0, l1)
        d2 = h2 = ListNode(0, l2)
        d3 = h3 = ListNode(0)
        accum = 0
        while h1.next or h2.next:
            v1 = h1.next.val if h1.next else 0
            v2 = h2.next.val if h2.next else 0
            s = v1 + v2 + accum
            h3.next = ListNode(s % 10)
            accum = s / 10
            h3 = h3.next
            if h1.next:
                h1 = h1.next
            if h2.next:
                h2 = h2.next
        if accum:
            h3.next = ListNode(accum)
        return d3.next
