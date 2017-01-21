"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        # Write your code here
        result = []
        if root is None:
            return result
        self.dfs(root, [str(root.val)], result)
        return result

    def dfs(self, node, path, result):
        if node.left is None and node.right is None:
            result.append('->'.join(path))
            return
        if node.left is not None:
            path.append(str(node.left.val))
            self.dfs(node.left, path, result)
            path.pop()
        if node.right is not None:
            path.append(str(node.right.val))
            self.dfs(node.right, path, result)
            path.pop()
