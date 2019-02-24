# https://leetcode.com/problems/maximum-binary-tree-ii
# Time: O(N)
# Space: avg O(logN), worst O(N). call stack

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        if val > root.val:
            node = TreeNode(val)
            node.left, root = root, node
        else:
            root.right = self.insertIntoMaxTree(root.right, val)
        return root
