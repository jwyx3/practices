"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param inorder : A list of integers that inorder traversal of a tree
    @param postorder : A list of integers that postorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder or len(inorder) != len(postorder):
            return None
        node = TreeNode(postorder[-1])
        pos = inorder.index(postorder[-1])
        node.left = self.buildTree(inorder[:pos], postorder[:pos])
        node.right = self.buildTree(inorder[pos + 1:], postorder[pos: -1])
        return node
