# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive(self, root):
        # Write your code here
        self.max_len = 0
        self.dfs(root)
        return self.max_len

    def dfs(self, node):
        if node is None:
            return 0
        left_len = self.dfs(node.left)
        right_len = self.dfs(node.right)

        node_len = 1
        if left_len > 0 and node.val + 1 == node.left.val:
            node_len = max(node_len, left_len + 1)
        if right_len > 0 and node.val + 1 == node.right.val:
            node_len = max(node_len, right_len + 1)

        if self.max_len < node_len:
            self.max_len = node_len

        return node_len
