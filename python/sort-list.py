class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    # merge sort
    def sortList(self, head):
        if not head or not head.next:
            return head
        mid = self.findMiddle(head)
        h1 = self.sortList(mid.next)
        mid.next = None
        h2 = self.sortList(head)
        return self.merge(h1, h2)

    def merge(self, h1, h2):
        curt = dummy = ListNode(0)
        while h1 and h2:
            if h1.val < h2.val:
                curt.next = h1
                h1 = h1.next
            else:
                curt.next = h2
                h2 = h2.next
            curt = curt.next
        if h1:
            curt.next = h1
        else:
            curt.next = h2
        return dummy.next

    # d->1->3->2->null
    def findMiddle(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution1:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    # quick sort
    def sortList(self, head):
        if not head or not head.next:
            return head
        mid = self.findMiddle(head)
        hl, hm, hr = self.partition(head, mid)
        hl = self.sortList(hl)
        hr = self.sortList(hr)
        return self.concat(hl, hm, hr)

    # d->1->3->2->end
    # use this template to find middle in list
    def findMiddle(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def findTail(self, head):
        # handle head is None
        while head and head.next:
            head = head.next
        return head

    # partition to three lists
    def partition(self, head, mid):
        dl, dm, dr = ListNode(0), ListNode(0), ListNode(0)
        tl, tm, tr = dl, dm, dr
        while head:
            if head.val < mid.val:
                tl.next = head
                tl = tl.next
            elif head.val > mid.val:
                tr.next = head
                tr = tr.next
            else:
                tm.next = head
                tm = tm.next
            head = head.next
        tl.next = tm.next = tr.next = None
        return dl.next, dm.next, dr.next

    # quick sort of list need to handle concat
    def concat(self, hl, hm, hr):
        dummy = tail = ListNode(0)
        for head in [hl, hm, hr]:
            tail.next = head
            tail = self.findTail(tail)
        return dummy.next


