# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
# Time: O(NlogN)
# Space: O(1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        # [lo, hi)
        def helper(lo, hi):
            if lo >= hi:
                return None
            target = preorder[lo]
            root = TreeNode(target)
            mid = lo + 1
            while mid < hi and preorder[mid] < target:
                mid += 1
            root.left = helper(lo + 1, mid)
            root.right = helper(mid, hi)
            return root
        
        return helper(0, len(preorder))
        
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/discuss/252232/JavaC%2B%2BPython-O(N)
# because len(A) <= 100.
# Time: O(100).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        self.idx = 0
        n = len(preorder)
        
        # [lo, hi]
        def helper(lo, hi):
            if self.idx == n or preorder[self.idx] < lo or preorder[self.idx] > hi:
                return None
            root = TreeNode(preorder[self.idx])
            self.idx += 1
            root.left = helper(lo, root.val)
            root.right = helper(root.val, hi)
            return root
    
        return helper(1, 100)
