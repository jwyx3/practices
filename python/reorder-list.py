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
    @return: nothing
    """
    def reorderList(self, head):
        if not head or not head.next:
            return
        mid = self.findMiddle(head)
        tail = self.reverse(mid.next)
        mid.next = None
        self.merge(head, tail)

    def merge(self, l1, l2):
        curt = dummy = ListNode(0)
        flag = True
        while l1 and l2:
            if flag:
                curt.next = l1
                l1 = l1.next
            else:
                curt.next = l2
                l2 = l2.next
            curt = curt.next
            flag = not flag
        if l1:
            curt.next = l1
        else:
            curt.next = l2
        return dummy.next

    def reverse(self, head):
        prev, curt = None, head
        while curt:
            next_node = curt.next
            curt.next = prev
            prev, curt = curt, next_node
        return prev

    # e.g.
    # d->1->2->3->4->null
    # slow: 2, fast: 4
    # d->1->2->3->null
    # slow: 2, fast: null
    # d->1->2->3->4->5->null
    # slow: 3, fast: null
    def findMiddle(self, head):
        slow = fast = ListNode(0, head)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        return slow
