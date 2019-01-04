# https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.h = []
        self.k = k
        for num in nums:
            heapq.heappush(self.h, num)
            if len(self.h) > k:
                heapq.heappop(self.h)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        elif val > self.h[0]:
            heapq.heappushpop(self.h, val)
        return self.h[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
