"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import copy
class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    # divide and conquer
    # find A and B, return LCA
    # find A, return A
    # find B, return B
    # not find, return None
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if root is None or root == A or root == B:
            return root

        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)

        if left is not None and right is not None:
            return root
        if left is not None:
            return left
        if right is not None:
            return right
        return None


