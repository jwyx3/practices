# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
# Time: O(N)
# Space: O(h), height of tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        MOD = 10**9 + 7
        ans = [0]
        
        def helper(node, path):
            if not node:
                return
            path.append(str(node.val))
            if not node.left and not node.right:
                ans[0] += int(''.join(path), 2) % MOD
                path.pop()
                return
            helper(node.left, path)
            helper(node.right, path)
            path.pop()
        
        helper(root, [])
        return ans[0] % MOD

