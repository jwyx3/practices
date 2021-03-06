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
    # recursion
    def preorderTraversal(self, root):
        return self.dfs(root)

    def dfs(self, root):
        if not root:
            return []
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return [root.val] + left + right

    # non-recursion
    def preorderTraversal1(self, root):
        if not root:
            return []
        ans, stack = [], [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ans
