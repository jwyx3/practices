# idea: 1) head may change, use dummy
#       2) add node, use tail
#       3) get min from list, use heapq
#       4) get next element of specific list, save head in heap

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        h = []
        for head in lists:
            if head:
                heapq.heappush(h, (head.val, head))
        result = []
        dummy = tail = ListNode(0)
        while h:
            _, curt = heapq.heappop(h)
            tail.next = curt
            tail = tail.next
            if curt.next:
                heapq.heappush(h, (curt.next.val, curt.next))
        return dummy.next
