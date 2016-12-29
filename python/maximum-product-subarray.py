class Solution:
    # @param nums: an integer[]
    # @return: an integer

    # dp_max[i]: the max product of the subarray with element i
    # dp_min[i]: the min product of the subarray with element i
    # dp_max, dp_min = max(dp_max * A[i], dp_min * A[i], A[i]), min(dp_max * A[i], dp_min * A[i], A[i])
    # initial: dp[0] = A[0]
    # ans: max(dp[...])
    def maxProduct(self, nums):
        n, A = len(nums), nums
        ans, dp_min, dp_max = A[0], A[0], A[0]
        for i in xrange(1, n):
            new_max, new_min = dp_max * A[i], dp_min * A[i]
            dp_max, dp_min = max(new_max, new_min, A[i]), min(new_max, new_min, A[i])
            ans = max(ans, dp_max)
        return ans

if __name__ == '__main__':
    s = Solution()
    print s.maxProduct([1,0,-1,2,3,-5,-2]), '#', '60'
