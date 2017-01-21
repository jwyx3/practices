"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def flatten(self, root):
        # write your code here
        self.dfs(root)

    def dfs(self, node):
        if node is None:
            return None

        left_end = self.dfs(node.left)
        right_end = self.dfs(node.right)

        if left_end is not None:
            left_end.right = node.right
            node.right = node.left
            node.left = None

        if right_end is not None:
            return right_end

        if left_end is not None:
            return left_end

        return node
