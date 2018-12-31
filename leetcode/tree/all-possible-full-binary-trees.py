# https://leetcode.com/problems/all-possible-full-binary-trees/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N == 0: return [None]
        if N == 1: return [TreeNode(0)]
        res = []
        # the nodes in subtree must be odd
        for i in xrange(1, N - 1, 2):
            L = self.allPossibleFBT(i)
            R = self.allPossibleFBT(N - 1 - i)
            for l in L:
                for r in R:
                    node = TreeNode(0)
                    node.left, node.right = l, r
                    res.append(node)
        return res
            
