### traverse all nodes and remember the node with max value
# It can use DFS or BFS. BFS is better

# DFS: recursion, preorder traversal
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the max node
    def maxNode(self, root):
        _, node = self.dfs(root)
        return node

    def dfs(self, root):
        if not root:
            return -sys.maxint, None
        max_val, max_node = root.val, root
        left, left_max_node = self.dfs(root.left)
        if left > max_val:
            max_val, max_node = left, left_max_node
        right, right_max_node = self.dfs(root.right)
        if right > max_val:
            max_val, max_node = right, right_max_node
        return max_val, max_node


# BFS
from collections import deque


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the max node
    def maxNode(self, root):
        if not root:
            return None
        q = deque([root])
        max_val, max_node = -sys.maxint, None
        while q:
            curt = q.popleft()
            if curt.val > max_val:
                max_val, max_node = curt.val, curt
            if curt.left:
                q.append(curt.left)
            if curt.right:
                q.append(curt.right)
        return max_node


# preorder traversal: non-recursion
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the max node
    def maxNode(self, root):
        if not root:
            return None
        stack = [root]
        max_val, max_node = -sys.maxint, None
        while stack:
            curt = stack.pop()
            if curt.val > max_val:
                max_val, max_node = curt.val, curt
            if curt.right:
                stack.append(curt.right)
            if curt.left:
                stack.append(curt.left)
        return max_node
