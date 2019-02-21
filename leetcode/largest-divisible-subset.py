# https://leetcode.com/problems/largest-divisible-subset/
# Time: O(N*N)
# Space: O(N)

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        N = len(nums)
        # dp[i]: the number of max subset including nums[i]
        # dp[i] = max(dp[i], dp[j] + 1), j < i and nums[j] % nums[i] == 0.
        # sort nums into descending
        # initial: dp[i] = i
        # answer: max(dp[i])
        # -> convert into path
        dp = [1] * N
        best, max_size = 0, 1
        nums.sort(reverse=True)
        path = range(N)
        for i in xrange(N):
            for j in xrange(i):
                if nums[j] % nums[i] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        path[i] = j
            if dp[i] > max_size:
                max_size = dp[i]
                best = i
        res, prev = [], -1
        while prev != best:
            res.append(nums[best])
            prev = best
            best = path[best]
        return res
