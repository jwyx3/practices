"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        father, curt, is_left = None, root, True
        while curt:
            father = curt
            if node.val < curt.val:
                curt = curt.left
                is_left = True
            else:
                curt = curt.right
                is_left = False
        if father:
            if is_left:
                father.left = node
            else:
                father.right = node
            return root
        return node
