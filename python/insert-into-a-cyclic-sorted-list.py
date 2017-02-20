"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    # @param {ListNode} node a list node in the list
    # @param {int} x an integer
    # @return {ListNode} the inserted new list node
    def insert(self, node, x):
        # one node case
        if node is None:
            ans = ListNode(x)
            ans.next = ans
            return ans

        curt, pre = node, None
        while True:
            pre = curt
            curt = curt.next
            # normal increasing order
            if pre.val <= x and curt.val >= x:
                break
            # the point with reversed order
            if curt.val < pre.val and (x >= pre.val or x <= curt.val):
                break
            # one node case
            if curt == node:
                break
        pre.next = ListNode(x, curt)
        return pre.next
