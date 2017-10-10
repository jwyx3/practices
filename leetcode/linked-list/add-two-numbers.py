# idea: 1) use dummy to remember head (head may change)
#       2) use tail to add new node
#       3) while l1 or l2: to reduce code
#       4) check carry at the final
#       5) basic idea of add: s = carry + n1 + n2

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = tail = ListNode(0)
        carry = 0
        while l1 or l2:
            s1 = l1.val if l1 else 0
            s2 = l2.val if l2 else 0
            carry += s1 + s2
            tail.next = ListNode(carry % 10)
            tail = tail.next
            carry /= 10
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        if carry:
            tail.next = ListNode(carry)
        return dummy.next
