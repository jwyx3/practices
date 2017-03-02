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
        self.dfs(root)

    # return tail
    def dfs(self, root):
        if not root:
            return None
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if left:
            left.right = root.right
            root.right = root.left
            # remember this!!
            root.left = None
        if right:
            return right
        if left:
            return left
        return root
