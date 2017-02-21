from heapq import heappush, heappop


class Solution:
    # @param nums {int[]} an integer unsorted array
    # @param k {int} an integer from 1 to n
    # @return {int} the kth largest element

    # heap
    def kthLargestElement2(self, nums, k):
        # Write your code here
        if not nums or k <= 0:
            return None
        h = []
        for num in nums:
            heappush(h, num)
            if len(h) > k:
                heappop(h)
        return h[0]

    # quick select
