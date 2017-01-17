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
        # write your code here
        self.stack = []
        self.node = root

    #@return: True if there has next node, or false
    def hasNext(self):
        # write your code here
        return self.node is not None or len(self.stack) > 0

    #@return: return next node
    def next(self):
        #write your code here
        while self.node is not None:
            self.stack.append(self.node)
            self.node = self.node.left

        self.node = self.stack.pop()
        ans = self.node
        self.node = self.node.right
        return ans
