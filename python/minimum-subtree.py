"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution1:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the root of the minimum subtree
    def findSubtree(self, root):
        # Write your code here
        if not root:
            return root

        self.min_sum = None
        self.min_node = None
        self.dfs(root)
        return self.min_node

    def dfs(self, node):
        if node is None:
            return 0
        left_sum = self.dfs(node.left)
        right_sum = self.dfs(node.right)
        node_sum = left_sum + right_sum + node.val

        if self.min_sum is None or self.min_sum > node_sum:
            self.min_sum = node_sum
            self.min_node = node

        return node_sum

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Result(object):
    def __init__(self, min_total, total, root):
        self.min_total = min_total
        self.total = total
        self.root = root


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the root of the minimum subtree
    def findSubtree(self, root):
        ans = self.dfs(root)
        return ans.root

    def dfs(self, root):
        if not root:
            return Result(sys.maxint, 0, root)
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        total = root.val + left.total + right.total
        ans = Result(total, total, root)
        if ans.min_total > left.min_total:
            ans = Result(left.min_total, total, left.root)
        if ans.min_total > right.min_total:
            ans = Result(right.min_total, total, right.root)
        return ans
