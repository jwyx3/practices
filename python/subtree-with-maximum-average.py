"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the root of the maximum average of subtree
    def findSubtree2(self, root):
        if not root:
            return root
        self.maxAve = None
        self.maxNode = None
        self.dfs(root)
        return self.maxNode

    def dfs(self, node):
        if node is None:
            return 0, 0

        leftSum, leftNum = self.dfs(node.left)
        rightSum, rightNum = self.dfs(node.right)
        nodeSum = leftSum + rightSum + node.val
        nodeNum = leftNum + rightNum + 1

        if self.maxAve is None or self.maxAve < 1.0 * nodeSum / nodeNum:
            self.maxAve = 1.0 * nodeSum / nodeNum
            self.maxNode = node

        return nodeSum, nodeNum
