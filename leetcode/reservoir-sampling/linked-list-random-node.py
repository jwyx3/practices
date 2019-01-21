# https://leetcode.com/problems/linked-list-random-node
# https://leetcode.com/problems/linked-list-random-node/discuss/85659/Brief-explanation-for-Reservoir-Sampling
# p = k/k+i, i=1..N-k

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        res, node, i = self.head.val, self.head, 0
        while node:
            # prob: k/k+i, k = 1
            if random.randint(0, i) == 0:
                res = node.val
            node = node.next
            i += 1
        return res
                
            
# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
