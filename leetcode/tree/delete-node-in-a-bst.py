# https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None

        # root may be changed
        dummy = parent = TreeNode(0)
        dummy.left = root

        # find target
        node = root
        while node:
            if node.val == key:
                break
            elif node.val > key:
                parent = node
                node = node.left
            else:
                parent = node
                node = node.right

        if not node:
            return root

        # left and right are present
        if node.left and node.right:
            new_node, parent = node.right, node
            while new_node.left:
                parent = new_node
                new_node = new_node.left
            node.val, node = new_node.val, new_node        
        
        # one child or no child
        if node.left:
            new_node = node.left
        else:
            new_node = node.right
        if parent.left == node:
            parent.left = new_node
        else:
            parent.right = new_node
            
        return dummy.left
