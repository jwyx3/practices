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
    def maxDepth(self, root):
        # write your code here
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
