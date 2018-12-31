# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        return self.helper(pre, post, 0, len(pre) - 1, 0, len(post) - 1)

    def find_index(self, post, start, target):
        for i in xrange(start, len(post)):
            if post[i] == target:
                return i
        return -1
        
    def helper(self, pre, post, s1, e1, s2, e2):
        if s1 > e1:
            return None
        node = TreeNode(pre[s1])
        if s1 == e1:
            return node
        # length of left subtree
        llen = self.find_index(post, s2, pre[s1 + 1]) - s2 + 1 
        node.left = self.helper(pre, post, s1 + 1, s1 + llen, s2, s2 + llen - 1)
        node.right = self.helper(pre, post, s1 + llen + 1, e1, s2 + llen, e2 - 1)
        return node
        
