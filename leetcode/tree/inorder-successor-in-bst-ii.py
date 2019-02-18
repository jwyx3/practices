# https://leetcode.com/problems/inorder-successor-in-bst-ii/
# https://leetcode.com/problems/inorder-successor-in-bst-ii/discuss/231587/Java-find-in-parents-or-find-in-descendents
# check right and parent

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
"""
class Solution(object):
    def inorderSuccessor(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node.right:
            curr = node.right
            while curr.left:
                curr = curr.left
            return curr
        else:
            curr = node.parent
            while curr and curr.val < node.val:
                curr = curr.parent
            return curr

