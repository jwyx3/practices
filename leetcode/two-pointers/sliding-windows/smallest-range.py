# credit: https://leetcode.com/problems/smallest-range/solution/
# idea: next array save current index of nums
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        if not nums: return []
        nexts = [0] * len(nums)
        # initialize with first elements
        h = [(nums[i][0], i) for i in xrange(len(nums))]
        max_v = max(x[0] for x in h)
        result = [0, sys.maxint]
        heapq.heapify(h)
        while h:
            # keep pop out min
            min_v, min_i = heapq.heappop(h)
            # update result if range is smaller
            if max_v - min_v < result[1] - result[0]:
                result = [min_v, max_v]
            nexts[min_i] += 1
            # cannot find valid tuple
            if nexts[min_i] == len(nums[min_i]):
                break
            # push the element from poped list back
            num = nums[min_i][nexts[min_i]]
            heapq.heappush(h, (num, min_i))
            # update max
            max_v = max(max_v, num)
        return result

