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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        def dfs(node):
            if node is None:
                return []
            result = [node.val]
            if node.left:
                result.extend(dfs(node.left))
            if node.right:
                result.extend(dfs(node.right))
            return result

        return dfs(root)

