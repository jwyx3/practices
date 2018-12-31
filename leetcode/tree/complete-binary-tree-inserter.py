# https://leetcode.com/problems/complete-binary-tree-inserter/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.q = collections.deque([root])
        self.parent = None
        while self.q:
            self.parent = self.q.popleft()
            if not self.parent.left:
                break
            self.q.append(self.parent.left)   
            if not self.parent.right:
                break
            self.q.append(self.parent.right)

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        node = TreeNode(v)
        res = self.parent
        self.q.append(node)
        if not self.parent.left:
            self.parent.left = node
        elif not self.parent.right:
            self.parent.right = node
            self.parent = self.q.popleft()
        return res.val
        
    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root 
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
