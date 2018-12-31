# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

# divide and conquer

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        head, tail = self.helper(root)
        if head and tail:
            head.left = tail
            tail.right = head
        return head
        
        
    # return smallest, largest
    def helper(self, root):
        if not root:
            return None, None
        ls, ll = self.helper(root.left)
        rs, rl = self.helper(root.right)
        if ll:
            ll.right = root
        if not ls:
            ls = root
        if rs:
            rs.left = root
        if not rl:
            rl = root
        root.left = ll    
        root.right = rs
        return ls, rl

# traveral

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.prev = dummy = Node(0, None, None)
        self.helper(root)
        head, tail = dummy.right, self.prev
        if head and tail:
            head.left, tail.right = tail, head
        return head

    # return smallest, largest
    def helper(self, root):
        if not root:
            return
        self.helper(root.left)
        self.prev.right = root
        root.left = self.prev
        self.prev = root
        self.helper(root.right)
