# https://leetcode.com/problems/binary-tree-pruning/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if self.isZero(root):
            return None
        return root
        
    
    # prune 0-subtree and return whether this is 0-subtree
    def isZero(self, root):
        if not root:
            return True
        L = self.isZero(root.left)
        R = self.isZero(root.right)
        if L: root.left = None
        if R: root.right = None
        return root.val == 0 and L and R
