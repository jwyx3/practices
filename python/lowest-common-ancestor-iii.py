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
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        a_exist, b_exist, node = self.dfs(root, A, B)
        if a_exist and b_exist:
            return node
        return None

    def dfs(self, node, A, B):
        if node is None:
            return False, False, None

        left_a_exist, left_b_exist, left = self.dfs(node.left, A, B)
        right_a_exist, right_b_exist, right = self.dfs(node.right, A, B)

        a_exist = left_a_exist or right_a_exist or node == A
        b_exist = left_b_exist or right_b_exist or node == B

        if node == A or node == B:
            return a_exist, b_exist, node
        if left and right:
            return a_exist, b_exist, node
        if left:
            return a_exist, b_exist, left
        if right:
            return a_exist, b_exist, right
        return a_exist, b_exist, None
