# https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        n = self.getLen(root)
        quot, rem = divmod(n, k)
        dummay = ListNode(0)
        dummay.next = root
        res = []
        for _ in xrange(k):
            m = quot + int(rem > 0)
            res.append(dummay.next)
            tail = dummay
            for _ in xrange(m):
                tail = tail.next
            dummay.next = tail.next
            tail.next = None
            rem -= 1
        return res
            
    def getLen(self, node):
        res = 0
        while node:
            res += 1
            node = node.next
        return res
