# Definition for a multi tree node.
# class MultiTreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         children = [] # children is a list of MultiTreeNode

class Solution:
    # @param {MultiTreeNode} root the root of k-ary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive3(self, root):
        self.max_length = 0
        self.dfs(root)
        return self.max_length

    # return the length of the longest consecutive sequence
    # (start from root, end with root)
    def dfs(self, root):
        if not root:
            return 0, 0
        length, len_from_root, len_to_root = 1, 1, 1
        lens_from = [1 for _ in range(len(root.children))]
        lens_to = [1 for _ in range(len(root.children))]

        max_len_from, max_len_to = 1, 1
        for i, child in enumerate(root.children):
            len_from_child, len_to_child = self.dfs(child)
            if len_from_child > 0 and root.val + 1 == child.val:
                lens_from[i] = len_from_child + 1
                len_from_root = max(len_from_root, lens_from[i])
                length = max(length, max_len_to + len_from_child)
            if len_to_child > 0 and root.val == child.val + 1:
                lens_to[i] = len_to_child + 1
                len_to_root = max(len_to_root, lens_to[i])
                length = max(length, max_len_from + len_to_child)
            max_len_from = max(max_len_from, lens_from[i])
            max_len_to = max(max_len_to, lens_to[i])
        if length > self.max_length:
            self.max_length = length
        return len_from_root, len_to_root
