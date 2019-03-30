# https://leetcode.com/problems/quad-tree-intersection/

"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object):
    def intersect(self, root1, root2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        if root1.isLeaf:
            return root1 if root1.val else root2
        if root2.isLeaf:
            return root2 if root2.val else root1
        root = Node(None, False, None, None, None, None)
        root.topLeft = self.intersect(root1.topLeft, root2.topLeft)
        root.topRight = self.intersect(root1.topRight, root2.topRight)
        root.bottomLeft = self.intersect(root1.bottomLeft, root2.bottomLeft)
        root.bottomRight = self.intersect(root1.bottomRight, root2.bottomRight)
        # combine all leaves
        if (root.topLeft.isLeaf and root.topRight.isLeaf and
                root.bottomLeft.isLeaf and root.bottomRight.isLeaf and
                root.topLeft.val == root.topRight.val == root.bottomLeft.val == root.bottomRight.val):
            root = Node(root.topLeft.val, True, None, None, None, None)
        return root
