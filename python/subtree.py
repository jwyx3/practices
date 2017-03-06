"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
    def isSubtree(self, T1, T2):
        t1 = self.serialize(T1)
        t2 = self.serialize(T2)
        return t1.find(t2) >= 0

    # preorder: make sure the whole subtree is a string
    def serialize(self, root):
        if not root:
            return '#'
        stack, rt = [root], []
        while stack:
            top = stack.pop()
            if top:
                rt.append(str(top.val))
                stack.append(top.right)
                stack.append(top.left)
            else:
                rt.append('#')
        return ''.join(rt)
