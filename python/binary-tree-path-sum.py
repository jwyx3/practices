"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths

    # traverse
    def binaryTreePathSum(self, root, target):
        if not root:
            return []
        ans = []
        self.dfs(root, [root.val], target - root.val, ans)
        return ans

    # path include root
    def dfs(self, root, path, target, result):
        if not root.left and not root.right:
            if target == 0:
                result.append(path[:])
            return
        if root.left:
            path.append(root.left.val)
            self.dfs(root.left, path, target - root.left.val, result)
            path.pop()
        if root.right:
            path.append(root.right.val)
            self.dfs(root.right, path, target - root.right.val, result)
            path.pop()

