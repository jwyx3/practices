import sys

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """
    # O(nlogn)
    def subarraySumClosest(self, nums):
        if not nums:
            return None
        sums, n = [0], len(nums)
        for s in xrange(1, n+1):
            sums.append(sums[s-1] + nums[s-1])
        # O(nlogn)
        sorted_sums = sorted([(sums[i], i) for i in xrange(len(sums))])
        ans, min_diff = None, sys.maxint
        for i in xrange(n):
            diff = abs(sorted_sums[i+1][0] - sorted_sums[i][0])
            if diff < min_diff:
                min_diff = diff
                ans = sorted([sorted_sums[i+1][1], sorted_sums[i][1]])
                ans[1] -= 1
        return ans
