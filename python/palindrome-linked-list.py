# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def isPalindrome(self, head):
        if not head:
            return True
        mid = self.findMiddle(head)
        # it will break original list
        mid.next = self.reverse(mid.next)

        p1, p2 = head, mid.next
        while p1 and p2 and p1.val == p2.val:
            p1 = p1.next
            p2 = p2.next
        return p2 is None

    # 1->2->3, return 2
    # 1->2->3->4, return 2
    def findMiddle(self, head):
        if not head:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev, head = head, temp
        return prev
