# https://leetcode.com/problems/linked-list-components/
# https://leetcode.com/problems/linked-list-components/solution/
# use state grouping; if grouping from False to True, res += 1
# Time: O(N + len(G))
# Space: O(len(G))

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        gset = set(G)
        grouping = False
        res = 0
        while head:
            if not grouping and head.val in gset:
                grouping = True
                res += 1
            elif grouping and head.val not in gset:
                grouping = False
            head = head.next
        return res
