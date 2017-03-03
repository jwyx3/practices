"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node
"""
class BSTIterator:
    #@param root: The root of binary tree.
    def __init__(self, root):
        self.stack = []
        self.node = root

    #@return: True if there has next node, or false
    def hasNext(self):
        return self.node or len(self.stack) > 0

    #@return: return next node
    def next(self):
        while self.node:
            self.stack.append(self.node)
            self.node = self.node.left
        node = self.stack.pop()
        self.node = node.right
        return node
