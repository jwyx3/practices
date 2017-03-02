"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
import copy
class Solution:
    """
    @param {TreeNode} root The root of the binary tree.
    @param {TreeNode} A and {TreeNode} B two nodes
    @return Return the LCA of the two nodes.
    """
    # return (a_exist, b_exist, None, A, B or LCA)
    def lowestCommonAncestor3(self, root, A, B):
        a_exist, b_exist, node = self.dfs(root, A, B)
        if a_exist and b_exist:
            return node
        return None

    def dfs(self, root, A, B):
        if not root:
            return False, False, None

        left_a_exist, left_b_exist, left = self.dfs(root.left, A, B)
        right_a_exist, right_b_exist, right = self.dfs(root.right, A, B)

        a_exist = left_a_exist or right_a_exist or root == A
        b_exist = left_b_exist or right_b_exist or root == B

        # If both A and B are found, they are locating at both subtrees
        if root == A or root == B:
            return a_exist, b_exist, root
        elif left and right:
            return a_exist, b_exist, root
        elif left:
            return a_exist, b_exist, left
        elif right:
            return a_exist, b_exist, right
        return a_exist, b_exist, None

