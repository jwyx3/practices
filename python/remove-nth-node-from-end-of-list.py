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
    @param n: An integer.
    @return: The head of linked list.
    """
    # assume that n <= length of list
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        pre, curt, tail = dummy, head, head
        for i in range(n):
            tail = tail.next
        while tail:
            pre = pre.next
            curt = curt.next
            tail = tail.next
        pre.next = curt.next
        return dummy.next
