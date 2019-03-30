# https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/
# https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/solution/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        N = len(voyage)
        counter = [0] * (N + 1)
        def count(root):
            if not root:
                return 0
            counter[root.val] = 1 + count(root.left) + count(root.right)
            return counter[root.val]
        
        count(root)
        res = []
        def match(root, voyage, lo, hi):
            if not root:
                return lo > hi
            if root.val != voyage[lo]:
                return False
            lval = counter[root.left.val if root.left else 0]
            rval = counter[root.right.val if root.right else 0]
            
            if match(root.left, voyage, lo + 1, lo + lval) and match(root.right, voyage, lo + lval + 1, hi):
                return True
            if match(root.left, voyage, lo + rval + 1, hi) and match(root.right, voyage, lo + 1, lo + rval):
                res.append(root.val)
                return True
            return False
        
        matched = match(root, voyage, 0, len(voyage) - 1)
        if not matched:
            return [-1]
        return res
