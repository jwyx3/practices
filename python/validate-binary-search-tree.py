"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

import collections
Result = collections.namedtuple('Result', 'is_bst min_val max_val')

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        def _is_valid_bst(node):
            if node is None:
                return Result(is_bst=True, min_val=None, max_val=None)
            left = _is_valid_bst(node.left)
            right = _is_valid_bst(node.right)
            is_bst = left.is_bst and right.is_bst and\
                        (left.max_val is None or left.max_val < node.val) and\
                        (right.min_val is None or right.min_val > node.val)

            min_val = max_val = node.val
            if left.min_val is not None:
                min_val = min(min_val, left.min_val)
            if right.max_val is not None:
                max_val = max(max_val, left.max_val)
            return Result(is_bst=is_bst, min_val=min_val, max_val=max_val)

        ans = _is_valid_bst(root)
        return ans.is_bst
