"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
from collections import deque


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list

    # BFS + level order traversal
    def binaryTreeToLists(self, root):
        if not root:
            return []
        q = deque([root])
        result = []
        while q:
            size = len(q)
            dummy = head = ListNode(0)
            for i in range(size):
                curt = q.popleft()
                head.next = ListNode(curt.val)
                head = head.next
                if curt.left:
                    q.append(curt.left)
                if curt.right:
                    q.append(curt.right)
            result.append(dummy.next)
        return result
