"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    # assume that 1 <= m <= n <= length of list
    def reverseBetween(self, head, m, n):
        dummy = ListNode(0, head)
        mth_prev = nth_next = dummy
        for i in range(1, n + 2):
            if i < m:
                mth_prev = mth_prev.next
            nth_next = nth_next.next
        mth = mth_prev.next

        # 1->2->3->4->5->NULL, m = 2, n = 4
        # => 1: mth_prev, 2: mth, 5: nth_next
        new_mth = self.reverse(mth, nth_next)
        mth_prev.next = new_mth
        mth.next = nth_next

        return dummy.next


    def reverse(self, head, end):
        prev, curt = None, head
        while curt != end:
            next_node = curt.next
            curt.next = prev
            prev, curt = curt, next_node
        return prev

