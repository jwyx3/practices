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
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        def _is_balanced(node):
            if node is None:
                return True, 0
            is_left_balanced, left_depth = _is_balanced(node.left)
            is_right_balanced, right_depth = _is_balanced(node.right)
            return is_left_balanced and is_right_balanced and abs(left_depth - right_depth) <= 1,\
                max(left_depth, right_depth) + 1

        ans, _ = _is_balanced(root)
        return ans

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Result(object):
    def __init__(self, balanced, height):
        self.balanced = balanced
        self.height = height


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        ans = self.dfs(root)
        return ans.balanced

    def dfs(self, root):
        if not root:
            return Result(True, 0)
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        balanced = left.balanced and right.balanced and\
            abs(left.height - right.height) <= 1
        height = max(left.height, right.height) + 1
        return Result(balanced, height)
