# https://leetcode.com/problems/k-empty-slots/
# dynamically find predecessor and successor
# BST is a good choice

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        if not flowers or k < 0:
            return -1
        root = TreeNode(flowers[0])
        for i in xrange(1, len(flowers)):
            node, parent = root, None
            v = flowers[i]
            new_node = TreeNode(v) 
            pred = succ = 0
            while node:
                parent = node
                if node.val > v:
                    succ = node.val
                    node = node.left
                else:
                    pred = node.val
                    node = node.right
            if parent.val > v:
                parent.left = new_node
            else:
                parent.right = new_node
            if pred and v - pred == k + 1 or succ and succ - v == k + 1:
                return i + 1
        return -1
                    
