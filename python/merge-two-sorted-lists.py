"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        head = dummy = ListNode('#')
        while l1 or l2:
            if not l1:
                head.next = l2
                break
            if not l2:
                head.next = l1
                break
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        return dummy.next
