# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head, a ListNode
    # @oaram {int} v1 an integer
    # @param {int} v2 an integer
    # @return {ListNode} a new head of singly-linked list
    def swapNodes(self, head, v1, v2):
        prev1 = prev2 = None
        curt = dummy = ListNode(0, head)
        while curt.next:
            if curt.next.val == v1:
                prev1 = curt
            elif curt.next.val == v2:
                prev2 = curt
            curt = curt.next
        if prev1 and prev2:
            node1, node2 = prev1.next, prev2.next
            prev1.next, prev2.next = node2, node1
            node1.next, node2.next = node2.next, node1.next
        return dummy.next
