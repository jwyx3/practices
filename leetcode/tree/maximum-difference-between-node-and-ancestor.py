# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
# Time: O(n), number of node
# Space: O(h), height of node

# bottom-up

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        # return (max, min, diff) of this tree
        def helper(node):
            ans = [node.val, node.val, 0]
            if not node.left and not node.right:
                return ans
            if node.left:
                left = helper(node.left)
                diff = max(abs(left[0] - node.val), abs(left[1] - node.val))
                lmin, lmax = min(left[0], ans[0]), max(left[1], ans[1])
                ans = [lmin, lmax, max(diff, left[-1], ans[-1])]
            if node.right:
                right = helper(node.right)
                diff = max(abs(right[0] - node.val), abs(right[1] - node.val))
                rmin, rmax = min(right[0], ans[0]), max(right[1], ans[1])
                ans = [rmin, rmax, max(diff, right[-1], ans[-1])]
            return ans
        
        ans = helper(root)
        return ans[-1]

# top-down
# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/discuss/274610/JavaC%2B%2BPython-Top-Down

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # mx: max value of ancestor
        # mn: min value of ancestor
        # return max V
        def helper(node, mx, mn):
            if not node:
                return 0
            ans = max(mx - node.val, node.val - mn)
            mx, mn = max(mx, node.val), min(mn, node.val)
            ans = max(ans, helper(node.left, mx, mn))
            ans = max(ans, helper(node.right, mx, mn))
            return ans
        
        return helper(root, root.val, root.val)
