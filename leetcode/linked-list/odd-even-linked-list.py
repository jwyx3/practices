# idea: 1) create two lists: use dummy and tail

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        d1 = t1 = ListNode(0)
        d2 = t2 = ListNode(0)
        idx = 0
        while head:
            if idx & 1:
                t2.next = ListNode(head.val)
                t2 = t2.next
            else:
                t1.next = ListNode(head.val)
                t1 = t1.next
            idx += 1
            head = head.next
        t1.next = d2.next
        return d1.next
