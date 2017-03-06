class Solution:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """

    # PrefixSum
    # space O(n)
    def minSubArray1(self, nums):
        if not nums:
            return 0
        sums = [0]
        for i in range(len(nums)):
            sums.append(sums[i] + nums[i])
        max_pre, ans = sums[0], sys.maxint
        for i in range(1, len(sums)):
            ans = min(ans, sums[i] - max_pre)
            max_pre = max(max_pre, sums[i])
        return ans

    # PrefixSum
    # space O(1)
    def minSubArray(self, nums):
        if not nums:
            return 0
        s, max_pre, ans = 0, 0, sys.maxint
        for i in range(len(nums)):
            s += nums[i]
            ans = min(ans, s - max_pre)
            max_pre = max(max_pre, s)
        return ans
