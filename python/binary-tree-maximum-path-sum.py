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
    def maxPathSum(self, root):
        # write your code here
        def dfs(node):
            if node is None:
                return -sys.maxint, 0
            left = dfs(node.left)
            right = dfs(node.right)
            max_path = max(left[0], right[0], left[1] + right[1] + node.val)
            # include node or not
            max_path_from_node = max(left[1] + node.val, right[1] + node.val, 0)
            return max_path, max_path_from_node
        ans, _ = dfs(root)
        return ans

