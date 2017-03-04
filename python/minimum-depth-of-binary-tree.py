"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def minDepth(self, root):
        if not root:
            return 0
        return self.dfs(root)

    def dfs(self, root):
        if not root.left and not root.right:
            return 1
        left = right = sys.maxint
        if root.left:
            left = self.dfs(root.left)
        if root.right:
            right = self.dfs(root.right)
        return min(left, right) + 1
