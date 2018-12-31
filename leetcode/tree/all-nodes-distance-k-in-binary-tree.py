# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# use node.parent
# Time: O(N), N is the amount of node
# Space: O(N)
class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        def dfs(node, parent):
            if not node:
                return
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root, None)
        
        res = []
        visited = set([target])
        q = collections.deque([(target, 0)])
        while q:
            if q[0][1] == K:
                res.extend([x[0].val for x in q])
                break
            node, dist = q.popleft()
            for child in (node.left, node.right, node.parent):
                if child and child not in visited:
                    q.append((child, dist + 1))
                    visited.add(child)
        return res

# don't use node.parent
# use divide and couquer
# if target not in its subtree: return -1
# if target in its subtree, return distance to target
# if root is target, return 0
class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        self.res = []
        self.helper(root, target, K)
        return self.res
        
    def helper(self, root, target, K):
        if not root: 
            return -1
        if root == target: 
            self.add_nodes(root, K)
            return 0
        L = self.helper(root.left, target, K)
        R = self.helper(root.right, target, K)
        if L >= 0:
            if K == L + 1:
                self.res.append(root.val)
            self.add_nodes(root.right, K - L - 2)
            return L + 1
        elif R >= 0:
            if K == R + 1:
                self.res.append(root.val)
            self.add_nodes(root.left, K - R - 2)
            return R + 1
        return -1
           
    def add_nodes(self, root, K):
        if not root or K < 0:
            return
        if K == 0: 
            self.res.append(root.val)
        else:
            self.add_nodes(root.left, K - 1)
            self.add_nodes(root.right, K - 1)
            
        

