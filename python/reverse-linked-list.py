"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list.
                  Reverse it in-place.
    """
    def reverse(self, head):
        prev, curt = None, head
        while curt:
            next_node = curt.next
            curt.next = prev
            prev, curt = curt, next_node
        return prev
