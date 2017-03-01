"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node
    """

    # divide and couquer
    def sortedListToBST(self, head):
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        mid_prev = self.findMiddlePrev(head)
        mid, mid_prev.next = mid_prev.next, None
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root

    # find the mid_prev
    # d->1->2->3->null
    # return 1
    def findMiddlePrev(self, head):
        slow, fast = ListNode(0, head), head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

