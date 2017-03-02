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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal1(self, root):
        return self.dfs(root)

    def dfs(self, root):
        if not root:
            return []
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return left + right + [root.val]

    def postorderTraversal(self, root):
        if not root:
            return []
        ans, stack, prev = [], [root], None
        while stack:
            curt = stack[-1]
            # traverse down
            if not prev or prev.left == curt or prev.right == curt:
                if curt.left:
                    stack.append(curt.left)
                elif curt.right:
                    stack.append(curt.right)
            # traverse up from left
            elif curt.left == prev:
                if curt.right:
                    stack.append(curt.right)
            else: # traverse up from right
                ans.append(curt.val)
                stack.pop()
            prev = curt
        return ans
