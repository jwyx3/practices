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
    @return: The node where the cycle begins.
                if there is no cycle, return null
    """
    def detectCycle(self, head):
        p1 = p2 = head
        while p1 and p2:
            p1 = p1.next
            p2 = p2.next
            if p2:
                p2 = p2.next
            if p2 and p1 == p2:
                break
        # found joint point
        if p2 and p1 == p2:
            p1 = head
            while p1 != p2:
                p1 = p1.next
                p2 = p2.next
            return p1
        return None


