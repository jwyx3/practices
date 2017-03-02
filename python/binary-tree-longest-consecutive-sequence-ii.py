# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive2(self, root):
        self.max_length = 0
        self.dfs(root)
        return self.max_length

    # return the length of the longest consecutive sequence
    # (start from root, end with root)
    def dfs(self, root):
        if not root:
            return 0, 0
        len_from_left, len_to_left = self.dfs(root.left)
        len_from_right, len_to_right = self.dfs(root.right)

        length, len1, len2 = 1, 1, 1
        len_from_root, len_to_root = 1, 1
        if len_to_left > 0 and root.val == root.left.val + 1:
            len1 += len_to_left
            len_to_root = max(len_to_root, len_to_left + 1)
        if len_from_right > 0 and root.val + 1 == root.right.val:
            len1 += len_from_right
            len_from_root = max(len_from_root, len_from_right + 1)
        if len_to_right > 0 and root.val == root.right.val + 1:
            len2 += len_to_right
            len_to_root = max(len_to_root, len_to_right + 1)
        if len_from_left > 0 and root.val + 1 == root.left.val:
            len2 += len_from_left
            len_from_root = max(len_from_root, len_from_left + 1)
        length = max(length, len1, len2)

        if length > self.max_length:
            self.max_length = length
        return len_from_root, len_to_root
