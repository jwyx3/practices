"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# traverse + divide and conquer
class Solution:
    # @param {TreeNode} root, the root of binary tree.
    # @return {int} The maximum amount of money you can rob tonight
    def houseRobber3(self, root):
        self.result = 0
        self.dfs(root)
        return self.result

    # return (
    #   max amount of money from root (including root),
    #   same as before (not including root)
    # )
    def dfs(self, root):
        if not root:
            return 0, 0
        left_money_node, left_money = self.dfs(root.left)
        right_money_node, right_money = self.dfs(root.right)
        # with root
        money_root = root.val + left_money + right_money
        # without root
        money = max(left_money_node, left_money) + max(right_money_node, right_money)
        self.result = max(self.result, money_root, money)
        return money_root, money
