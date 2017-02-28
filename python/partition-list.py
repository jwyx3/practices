"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param x: an integer
    @return: a ListNode
    """

    # d1: list of elements >= x
    # d2: list of elements < x
    # t1: point to the tail of d1
    # t2: point to the tail of d2
    def partition(self, head, x):
        d1, d2 = ListNode(0, head), ListNode(0)
        t1, t2 = d1, d2
        while t1.next:
            if t1.next.val < x:
                # add to tail of d2
                t2.next = t1.next
                # update tail of d2
                t2 = t2.next
                # remove element from d1
                t1.next = t1.next.next
            else:
                # update tail of d1
                t1 = t1.next
        # link d2 and d1
        t2.next = d1.next
        return d2.next
