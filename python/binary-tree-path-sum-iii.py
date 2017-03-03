"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""
class Solution:
    # @param {ParentTreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum3(self, root, target):
        ans = []
        self.dfs(root, target, ans)
        return ans

    # go through all nodes
    def dfs(self, root, target, result):
        if not root:
            return
        self.findSums(root, None, [], target, result)
        self.dfs(root.left, target, result)
        self.dfs(root.right, target, result)

    # start from root and find all paths with target sum
    def findSums(self, root, father, path, target, result):
        path.append(root.val)
        target -= root.val
        if target == 0:
            result.append(path[:])
        if root.parent and root.parent != father:
            self.findSums(root.parent, root, path, target, result)
        if root.left and root.left != father:
            self.findSums(root.left, root, path, target, result)
        if root.right and root.right != father:
            self.findSums(root.right, root, path, target, result)
        path.pop()
