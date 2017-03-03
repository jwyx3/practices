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
    def binaryTreePathSum2(self, root, target):
        ans = []
        self.dfs(root, [], 0, target, ans)
        return ans

    # path don't include root
    def dfs(self, root, path, level, target, result):
        if not root:
            return
        path.append(root.val)
        tmp = target
        for i in range(level, -1, -1):
            tmp -= path[i]
            if tmp == 0:
                result.append(path[i:])
        self.dfs(root.left, path, level + 1, target, result)
        self.dfs(root.right, path, level + 1, target, result)
        path.pop()

