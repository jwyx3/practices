"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    # use one queue
    def levelOrder(self, root):
        # write your code here
        result = []
        if root is None:
            return result
        q = [(root, 0)]
        while len(q) > 0:
            node, level = q.pop(0)
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
            if len(result) <= level:
                result.append([])
            result[-1].append(node.val)
        return result

    # use dfs
    def levelOrder(self, root):
        def dfs(node, level, result):
            if len(result) <= level:
                result.append([])
            result[level].append(node.val)
            if node.left:
                dfs(node.left, level + 1, result)
            if node.right:
                dfs(node.right, level + 1, result)
        result = []
        if root is None:
            return result
        dfs(root, 0, result)
        return result

