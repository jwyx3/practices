"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder or len(preorder) != len(inorder):
            return None
        node = TreeNode(preorder[0])
        pos = inorder.index(preorder[0])
        # NOTE: A[a:b+1] => A[a],...,A[b]
        node.left = self.buildTree(preorder[1:pos + 1], inorder[:pos])
        node.right = self.buildTree(preorder[pos + 1:], inorder[pos + 1:])
        return node
