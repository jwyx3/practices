# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    @param root <TreeNode>: The root of the BST.
    @param p <TreeNode>: You need find the successor node of p.
    @return <TreeNode>: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        node, successor_node, parent_node = root, None, None
        while node and node != p:
            if p.val < node.val:
                # the potential successor of left node is parent node
                successor_node = node
                next_node = node.left
            else:
                # the potential successor of right node is parent of parent node
                successor_node = parent_node
                next_node = node.right
            parent_node, node = node, next_node

        # p is not found
        if not node:
            return None

        # if right node of p is absent, successor node is found
        if not p.right:
            return successor_node

        # otherwise, get the most left successor of right substree
        node = p.right
        while node.left:
            node = node.left
        return node

