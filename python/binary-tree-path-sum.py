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
    def binaryTreePathSum(self, root, target):
        # Write your code here
        result = []
        if root is None:
            return result
        self.dfs(root, [root.val], root.val, target, result)
        return result

    def dfs(self, node, path, path_sum, target, result):
        if node.left is None and node.right is None:
            if path_sum == target:
                result.append(path[:])
            return

        if node.left is not None:
            path.append(node.left.val)
            self.dfs(node.left, path, path_sum + node.left.val, target, result)
            path.pop()

        if node.right is not None:
            path.append(node.right.val)
            self.dfs(node.right, path, path_sum + node.right.val, target, result)
            path.pop()

