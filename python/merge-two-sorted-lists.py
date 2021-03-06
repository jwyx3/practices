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
        curt = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curt.next = l1
                l1 = l1.next
            else:
                curt.next = l2
                l2 = l2.next
            curt = curt.next
        if l1:
            curt.next = l1
        if l2:
            curt.next = l2
        return dummy.next

