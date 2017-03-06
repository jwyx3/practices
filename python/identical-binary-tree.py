"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param a, b, the root of binary trees.
    @return true if they are identical, or false.
    """
    # divide and conquer
    def isIdentical(self, a, b):
        if a and not b or not a and b:
            return False
        if not a and not b:
            return True
        left = self.isIdentical(a.left, b.left)
        right = self.isIdentical(a.right, b.right)
        if a.val == b.val and left and right:
            return True
        return False
