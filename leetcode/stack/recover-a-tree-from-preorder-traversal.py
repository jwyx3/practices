# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/
# better one!!
# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/discuss/274621/JavaC%2B%2BPython-Iterative-Stack-Solution
# Time: O(n)
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        if not S:
            return None
        N = len(S)
        g_curr, g_depth = [0], [0]
        
        def get_num():
            num = 0
            while g_curr[0] < N and S[g_curr[0]].isdigit():
                num = 10 * num + int(S[g_curr[0]])
                g_curr[0] += 1
            return num
        
        def get_depth():
            if not g_depth[0]:
                depth = 0
                while g_curr[0] < N and S[g_curr[0]] == '-':
                    depth += 1
                    g_curr[0] += 1
                g_depth[0] = depth
            return g_depth[0]
        
        def helper(depth):
            root = TreeNode(get_num())
            ldepth = get_depth()
            if depth + 1 == ldepth:
                g_depth[0] = 0
                root.left = helper(ldepth)
            rdepth = get_depth()
            if depth + 1 == rdepth:
                g_depth[0] = 0
                root.right = helper(rdepth)
            return root
    
        return helper(0)
            
# Iterative version

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        if not S:
            return None
        i, stack = 0, []
        while i < len(S):
            level, val = 0, ''
            while i < len(S) and S[i] == '-':
                level += 1
                i += 1
            while i < len(S) and S[i] != '-':
                val += S[i]
                i += 1
            while len(stack) > level:
                stack.pop()
            node = TreeNode(int(val))
            if stack and stack[-1].left is None:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
