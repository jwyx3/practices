"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param root the root of binary tree.
    @return an integer
    """
    def maxPathSum2(self, root):
        # Write your code here
        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return max(left + node.val, right + node.val, node.val)
        return dfs(root)
