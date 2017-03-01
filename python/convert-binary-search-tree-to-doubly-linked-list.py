"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition of Doubly-ListNode
class DoublyListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = next
"""

class Solution:
    """
    @param root, the root of tree
    @return: a doubly list node
    """
    def bstToDoublyList(self, root):
        if not root:
            return None
        head, _ = self.dfs(root)
        return head

    def dfs(self, root):
        head = tail = node = DoublyListNode(root.val)
        if root.left:
            head, left = self.dfs(root.left)
            left.next = node
        if root.right:
            right, tail = self.dfs(root.right)
            node.next = right
        return head, tail

