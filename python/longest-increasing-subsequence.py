class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    # dp[i]: the length of the longest increasing subsequence with element i
    # dp[i] = max(dp[j]) + 1                # if any A[j] <= A[i], j < i
    #       = 1                             # otherwise
    # initial: dp[0] = 1
    # ans: max(dp[...])
    def longestIncreasingSubsequence(self, nums):
        if not nums:
            return 0
        n, A = len(nums), nums
        dp = [1] * n
        for i in xrange(1, n):
            for j in xrange(i):
                # not equal
                if A[j] < A[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    # TODO: O(nlogn)
    # binary search 找到插入位置
    # 插入元素组成最长递增子列
