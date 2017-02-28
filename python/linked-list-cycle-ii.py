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
        slow = fast = head
        while slow and fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            if fast and fast == slow:
                break
        if fast and fast == slow:
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return fast
        return None

