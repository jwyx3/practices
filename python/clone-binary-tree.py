"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param {TreeNode} root: The root of binary tree
    @return {TreeNode} root of new tree
    """

    # divide and conquer
    def cloneTree(self, root):
        if not root:
            return None
        node = TreeNode(root.val)
        node.left = self.cloneTree(root.left)
        node.right = self.cloneTree(root.right)
        return node
