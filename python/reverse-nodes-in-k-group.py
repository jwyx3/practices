# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode

    # n0 -> n1 -> n2 -> ... -> nk -> nk+1
    # n0 -> nk -> nk-1 -> ... -> n1 -> nk+1
    # prev_1th = n0, 1th = n1, kth = nk, kth_next = nk+1
    def reverseKGroup(self, head, k):
        dummy = ListNode(0, head)
        prev_first = dummy
        while True:
            first, kth = self.findNextK(prev_first, k)
            if not kth:
                break
            kth_next = kth.next
            self.reverse(first, kth_next)
            prev_first.next, first.next = kth, kth_next
            # update to next k
            prev_first = first
        return dummy.next

    # return 1th, kth
    def findNextK(self, prev_first, k):
        kth = prev_first
        for i in range(1, k + 1):
            if not kth:
                break
            kth = kth.next
        return prev_first.next, kth

    def reverse(self, head, end):
        prev, curt = None, head
        while curt != end:
            next_node = curt.next
            curt.next = prev
            prev, curt = curt, next_node
        return prev
