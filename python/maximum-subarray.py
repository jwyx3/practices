class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    # 贪心
    def maxSubArray(self, nums):
        if not nums:
            return 0
        ans, s = nums[0], max(nums[0], 0)
        for i in xrange(1, len(nums)):
            s += nums[i]
            ans = max(ans, s)
            # 扔掉负数的前缀和
            s = max(s, 0)
        return ans

    # 前缀和
    def maxSubArray(self, nums):
        if not nums:
            return 0
        ans, min_s, s = nums[0], min(nums[0], 0), nums[0]
        for i in xrange(1, len(nums)):
            s += nums[i]
            ans = max(ans, s - min_s)
            # 找到最小前缀和
            min_s = min(min_s, s)
        return ans

    # DP
    # dp[i]: 0 - i, 以i为结尾的最大序列和
    # dp[i]: max(dp[i - 1] + A[i], A[i])
    # initial: dp[0] = A[i]
    # ans: max(dp[0], ..., dp[len(A) - 1])
    def maxSubArray(self, nums):
        if not nums:
            return 0
        ans, dp = nums[0], [nums[0]]
        for i in xrange(1, len(nums)):
            dp.append(max(dp[i - 1] + nums[i], nums[i]))
            ans = max(ans, dp[i])
        return ans
