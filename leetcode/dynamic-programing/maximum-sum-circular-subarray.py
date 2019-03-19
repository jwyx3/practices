# https://leetcode.com/problems/maximum-sum-circular-subarray/
# https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/178422/One-Pass
# https://leetcode.com/problems/maximum-sum-circular-subarray/solution/
# Kadane's algorithm
# For a given array A, Kadane's algorithm can be used to find the maximum sum of the subarrays of A
# dp[i] be the maximum sum of a subarray that ends in A[i]
# dp[i] = A[i] + max(dp[i-1], 0)
# answer: max(dp)
#
# reduce space complexity
# res = max(dp), cur = dp[i]
#
# Kadane's algorithm
# res = cur = None
# for x in A:
#     cur = x + max(cur, 0)
#     res = max(res, cur)
# return res
#
# 1) how to use monoqueue
# 2) how to use kadane variant

class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # several ideas:
        # 1. 2*N array
        # 2. one subarray or two subarray
        # 3. max(one max subarray, one min subarray)
        # corner case: array at least has one element
        # min_ans may be empty
        if not A:
            return 0
        total = max_prev = min_prev = 0
        max_ans, min_ans = float('-inf'), float('inf')
        for num in A:
            total += num
            max_ans = max(max_ans, total - min_prev)
            min_ans = min(min_ans, total - max_prev)
            max_prev = max(max_prev, total)
            min_prev = min(min_prev, total)
        return max(max_ans, total - min_ans) if max_ans > 0 else max_ans
