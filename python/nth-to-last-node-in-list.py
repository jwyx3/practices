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
    @return: Nth to last node of a singly linked list.
    """
    def nthToLast(self, head, n):
        head = tail = ListNode(0, head)
        for _ in range(n):
            tail = tail.next
        while tail:
            tail = tail.next
            head = head.next
        return head
