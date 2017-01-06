"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
# 单调递减栈
class Solution:
    # @param A: Given an integer array with no duplicates.
    # @return: The root of max tree.
    def maxTree(self, A):
        stack = []
        for e in A:
            node = TreeNode(e)
            while len(stack) > 0 and e > stack[-1].val:
                node.left = stack.pop()
            if len(stack) > 0:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
