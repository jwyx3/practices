"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """
    def searchRange(self, root, k1, k2):
        ans = []
        self.dfs(root, k1, k2, ans)
        return ans

    def dfs(self, root, k1, k2, result):
        if not root:
            return
        if root.left and root.val > k1:
            self.dfs(root.left, k1, k2, result)
        if root.val >= k1 and root.val <= k2:
            result.append(root.val)
        if root.right and root.val <= k2:
            self.dfs(root.right, k1, k2, result)
