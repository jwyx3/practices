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
    @return: Inorder in ArrayList which contains node values.
    """
    # recursion
    def inorderTraversal(self, root):
        return self.dfs(root)

    def dfs(self, root):
        if not root:
            return []
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return left + [root.val] + right

    # non-recursion
    def inorderTraversal1(self, root):
        if not root:
            return []
        ans, stack, curt = [], [], root
        while curt or stack:
            while curt:
                stack.append(curt)
                curt = curt.left
            curt = stack.pop()
            ans.append(curt.val)
            curt = curt.right
        return ans
