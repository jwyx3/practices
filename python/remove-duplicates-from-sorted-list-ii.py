"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        dummy = prev = ListNode(0, head)
        curt = head
        while curt and curt.next:
            if curt.next and curt.val == curt.next.val:
                val = curt.val
                # find first element != val or None
                while curt and val == curt.val:
                    curt = curt.next
                prev.next = curt
            else:
                # go to next
                curt = curt.next
                prev = prev.next
        return dummy.next


