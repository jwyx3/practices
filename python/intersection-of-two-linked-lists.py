# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param headA: the first list
    # @param headB: the second list
    # @return: a ListNode
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        tailA = headA
        while tailA.next:
            tailA = tailA.next
        tailA.next = headB
        ans = self.detectCycle(headA)
        tailA.next = None
        return ans

    def detectCycle(self, head):
        fast = slow = head
        while fast and slow:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            if fast and fast == slow:
                break
        if fast and fast == slow:
            fast = head
            while slow != fast:
                fast = fast.next
                slow = slow.next
            return fast
        return None
