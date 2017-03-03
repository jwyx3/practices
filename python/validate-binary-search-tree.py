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
    @return: True if the binary tree is BST, or false
    """

    # BST definition: left < root and root <= right
    # but the definition of this problem: left < root and root < right
    # divide and conquer
    def isValidBST(self, root):
        is_bst, _, _ = self.dfs(root)
        return is_bst

    def dfs(self, root):
        if not root:
            return True, sys.maxint, -sys.maxint
        is_bst_left, min_left, max_left = self.dfs(root.left)
        is_bst_right, min_right, max_right = self.dfs(root.right)

        if not is_bst_left or not is_bst_right:
            return False, 0, 0
        if root.left and max_left >= root.val or\
                root.right and min_right <= root.val:
            return False, 0, 0
        return True, min(min_left, root.val), max(max_right, root.val)
