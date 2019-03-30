# solution
#   - BFS to find node with x
#   - if found x, keep search for first leaf node

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.leaf = None
        self.ldist = -1
        self.helper(root, k)
        return self.leaf.val
    
    # return dist between root and k
    def helper(self, root, k):
        if not root:
            return -1
        if root.val == k:
            self.find_leaf(root, 0)
            return 0
        L = self.helper(root.left, k)
        R = self.helper(root.right, k)
        if L >= 0:
            self.find_leaf(root.right, L + 2)
            return L + 1
        elif R >= 0:
            self.find_leaf(root.left, R + 2)
            return R + 1
        return -1
    
    def find_leaf(self, root, dist):
        if not root:
            return
        if not root.left and not root.right:
            if not self.leaf or dist < self.ldist:
                self.leaf = root
                self.ldist = dist
            return
        self.find_leaf(root.left, dist + 1)
        self.find_leaf(root.right, dist + 1)
