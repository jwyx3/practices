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
    @return: A list of list of integer include
             the zig zag level order traversal of its nodes' values
    """

    # BFS + level order traversal + flag
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        q = deque([root])
        result, flag = [], True
        while q:
            size = len(q)
            result.append([])
            for i in range(size):
                curt = q.popleft()
                if flag:
                    result[-1].append(curt.val)
                else:
                    result[-1].insert(0, curt.val)
                if curt.left:
                    q.append(curt.left)
                if curt.right:
                    q.append(curt.right)
            flag = not flag
        return result
