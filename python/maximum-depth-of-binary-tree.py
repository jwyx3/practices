"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class solution:
    """
    @param root: the root of binary tree.
    @return: an integer
    """
    def maxdepth(self, root):
        if not root:
            return 0
        left = self.maxdepth(root.left)
        right = self.maxdepth(root.right)
        return 1 + max(left, right)


class Solution1:
        def dfs(node, depth, result):
            if not node.left and not node.right:
                result['max_depth'] = max(result['max_depth'], depth)
            if node.left:
                dfs(node.left, depth + 1, result)
            if node.right:
                dfs(node.right, depth + 1, result)

        result = {'max_depth': 0}
        if root:
            dfs(root, 1, result)
        return result['max_depth']
