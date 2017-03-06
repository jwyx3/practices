"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param A: a list of integer
    @return: a tree node
    """
    def sortedArrayToBST(self, A):
        if not A:
            return None
        return self.buildTree(A, 0, len(A) - 1)

    def buildTree(self, A, left, right):
        if left > right:
            return None
        mid = left + (right - left) / 2
        node = TreeNode(A[mid])
        node.left = self.buildTree(A, left, mid - 1)
        node.right = self.buildTree(A, mid + 1, right)
        return node

