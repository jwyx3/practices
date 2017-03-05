"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

from collections import deque


class Solution:
    """
    @param root: The root of binary tree.
    @return: buttom-up level order in a list of lists of integers
    """

    # BFS + insert direction + level order traversal
    def levelOrderBottom(self, root):
        if not root:
            return []
        q = deque([root])
        result = []
        while q:
            size = len(q)
            result.insert(0, [])
            for i in range(size):
                curt = q.popleft()
                result[0].append(curt.val)
                if curt.left:
                    q.append(curt.left)
                if curt.right:
                    q.append(curt.right)
        return result

