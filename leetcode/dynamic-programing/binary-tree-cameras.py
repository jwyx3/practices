# https://leetcode.com/problems/binary-tree-cameras/
# https://leetcode.com/problems/binary-tree-cameras/solution/
# Time: O(N), N is node numbers
# Space: O(H), H is the height of root

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def solve(root):
            if not root: return 0, 0, float('inf')
            
            L = solve(root.left)
            R = solve(root.right)
            
            # children are covered but not root
            dp0 = L[1] + R[1]
            # children and root are covered, but no camera in root
            dp1 = min(L[2] + min(R[1:]), min(L[1:]) + R[2])
            # children and root are covered, and one camera in root
            dp2 = 1 + min(L) + min(R)
            
            return dp0, dp1, dp2
        
        return min(solve(root)[1:])

