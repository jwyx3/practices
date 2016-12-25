import heapq

class Solution:
    """
    @param nums: A list of integers.
    @return: The median of numbers
    """
    def medianII(self, nums):
        if not nums:
            return []

        ans, median = [], nums[0]
        # min_heap: >= median, max_heap: <= median
        min_heap, max_heap = [], []
        for a in nums:
            if a >= median:
                heapq.heappush(min_heap, a)
            else:
                heapq.heappush(max_heap, - a)

            while len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, - heapq.heappop(min_heap))
            while len(max_heap) > len(min_heap) + 1:
                heapq.heappush(min_heap, - heapq.heappop(max_heap))
            median = - max_heap[0]
            ans.append(median)
        return ans

if __name__ == '__main__':
    s = Solution()
    print s.medianII([1,2,3,4,5]), '#', "[1,1,2,2,3]"
