# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head: the list
    # @param k: rotate to the right k places
    # @return: the list after rotation

    # d->1->2->3->4->5
    # t1, t2: tail of two lists
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        k = k % self.getLen(head)
        dummy = ListNode(0, head)
        t1 = t2 = dummy
        for i in range(k):
            t2 = t2.next
        while t2.next:
            t2 = t2.next
            t1 = t1.next
        t2.next = dummy.next
        dummy.next = t1.next
        t1.next = None
        return dummy.next

    def getLen(self, head):
        size = 0
        while head:
            head = head.next
            size += 1
        return size

