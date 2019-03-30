# solution:
#   - in-order traversal get sorted list; t O(n), s O(n)
#   - binary search find the closest element x in list; t O(log n)
#   - start from x, search two directions to find k elements; t O(k)
#   => t O(n + k), s O(n)
#
# follow-up: 
#   Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
#
#   idea: only need to find closest element and search its k closest predecessor and successor
#
#   for leaf node, its parent must be its closest predecessor or successor
#
#   - find the closest element x in the tree; t O(log n)
#   - use two stacks to remember its predecessor and successor
#   - similar to merge sort, compare next predecessor and successor, get the closest k elements
#
# refer: https://leetcode.com/problems/closest-binary-search-tree-value-ii/discuss/70503/O(logN)-Java-Solution-with-two-stacks-following-hint

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def next_predecessor(self, node):
        res = []
        curr = node.left
        while curr:
            res.append(curr)
            curr = curr.right
        return res
    
    def next_successor(self, node):
        res = []
        curr = node.right
        while curr:
            res.append(curr)
            curr = curr.left
        return res
    
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        if not root or k <= 0:
            return []
        pred = []
        succ = []
        
        node = root
        while node:
            if target > node.val:
                pred.append(node)
                node = node.right
            else:
                succ.append(node)
                node = node.left
        
        res = []
        for _ in xrange(k):
            if pred and succ:
                pred_diff, succ_diff = abs(pred[-1].val - target), abs(succ[-1].val - target)
                if pred_diff < succ_diff:
                    res.append(pred[-1].val)
                    pred.extend(self.next_predecessor(pred.pop()))
                else:
                    res.append(succ[-1].val)
                    succ.extend(self.next_successor(succ.pop()))
            elif pred:
                res.append(pred[-1].val)
                pred.extend(self.next_predecessor(pred.pop()))
            else:
                res.append(succ[-1].val)
                succ.extend(self.next_successor(succ.pop()))
        return res

