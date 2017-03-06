"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque


class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing

    # walk every node and invert children
    # divide and conquer: recursion
    def invertBinaryTree1(self, root):
        if not root:
            return
        self.invertBinaryTree(root.left)
        self.invertBinaryTree(root.right)
        root.left, root.right = root.right, root.left

    # BFS: iterative
    def invertBinaryTree(self, root):
        if not root:
            return
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            node.left, node.right = node.right, node.left

