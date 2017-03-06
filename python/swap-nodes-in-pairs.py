# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        dummy = curt = ListNode(0, head)
        while curt.next and curt.next.next:
            n1, n2 = curt.next, curt.next.next
            # curt->n1->n2->n3
            # 1) curt->n2
            # 2) n1->n3
            # 3) n2->n1
            # 4) curt = n1
            curt.next = n2
            n1.next = n2.next
            n2.next = n1
            curt = n1
        return dummy.next
