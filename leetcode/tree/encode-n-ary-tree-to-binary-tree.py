# https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/
# https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/discuss/153061/Java-Solution-(Next-Level-greater-left-Same-Level-greater-right)

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
class Codec:

    def encode(self, root):
        """Encodes an n-ary tree to a binary tree.
        
        :type root: Node
        :rtype: TreeNode
        """
        if not root:
            return None
        # first child of node become left child of new root
        # the second child of node become right child of left child of new root
        # etc.
        node = TreeNode(root.val)
        if root.children:
            curr = node.left = self.encode(root.children[0])
            for child in root.children[1:]:
                curr.right = self.encode(child)
                curr = curr.right
        return node
        
    def decode(self, root):
        """Decodes your binary tree to an n-ary tree.
        
        :type root: TreeNode
        :rtype: Node
        """
        if not root:
            return None
        node = Node(root.val, [])
        if root.left:
            curr = root.left
            while curr:
                node.children.append(self.decode(curr))
                curr = curr.right
        return node
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
