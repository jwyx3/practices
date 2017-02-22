"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
import heapq


class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        h = []
        tail = dummy = ListNode(0)
        for lineId, node in enumerate(lists):
            if node:
                heapq.heappush(h, (node.val, node, lineId))
                lists[lineId] = node.next
        while len(h) > 0:
            _, curt, lineId = heapq.heappop(h)
            tail.next = curt
            tail = tail.next
            if lists[lineId]:
                node = lists[lineId]
                heapq.heappush(h, (node.val, node, lineId))
                lists[lineId] = node.next

        return dummy.next
