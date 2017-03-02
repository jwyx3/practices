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
        self.max_total = 0
        self.max_count = 0
        self.max_root = None
        self.dfs(root)
        return self.max_root

    def dfs(self, root):
        if not root:
            return 0, 0

        left_total, left_count = self.dfs(root.left)
        right_total, right_count = self.dfs(root.right)
        total = left_total + right_total + root.val
        count = left_count + right_count + 1

        if not self.max_root or\
                total * self.max_count > count * self.max_total:
            self.max_count = count
            self.max_total = total
            self.max_root = root

        return total, count

