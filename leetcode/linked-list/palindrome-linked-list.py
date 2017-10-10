# idea:
# 1) find_mid, revese, compare

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # find mid, reverse and compare
        if not head: return True
        mid = self.find_mid(head)
        h2 = self.reverse(mid.next)
        mid.next = None
        return self.compare(head, h2)

    def find_mid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head):
        prev = None
        while head:
            head_next = head.next
            head.next = prev
            prev, head = head, head_next
        return prev

    def compare(self, h1, h2):
        while h1 and h2:
            if h1.val != h2.val:
                return False
            h1 = h1.next
            h2 = h2.next
        return True
