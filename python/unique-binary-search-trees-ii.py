"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @paramn n: An integer
    # @return: A list of root

    # divide and conquer
    def generateTrees(self, n):
        return self.dfs(1, n)

    def dfs(self, start, end):
        if start > end:
            return [None]
        result = []
        for v in range(start, end + 1):
            left = self.dfs(start, v - 1)
            right = self.dfs(v + 1, end)
            for i in left:
                for j in right:
                    root = TreeNode(v)
                    root.left, root.right = i, j
                    result.append(root)
        return result

