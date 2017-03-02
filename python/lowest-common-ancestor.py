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

    # Assume two nodes are exist in tree.
    # return None or A or B or LCA
    def lowestCommonAncestor(self, root, A, B):
        if not root:
            return root
        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)
        if root == A or root == B:
            return root
        elif left and right:
            return root
        elif left:
            return left
        elif right:
            return right
        return None

