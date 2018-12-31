# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/ 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        res, _ = self.helper(root, 0)
        return res
        
    # return (the common ancestor node with the largest depth, the largest depth)
    def helper(self, root, depth):
        if not root:
            return None, -1
        lnode, ld = self.helper(root.left, depth + 1)
        rnode, rd = self.helper(root.right, depth + 1)
        node, d = root, depth
        if lnode and rnode:
            if ld == rd:
                node, d = root, ld
            elif ld > rd:
                node, d = lnode, ld
            else:
                node, d = rnode, rd
        elif lnode:
            node, d = lnode, ld
        elif rnode:
            node, d = rnode, rd
        return node, d
        
