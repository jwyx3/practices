class Solution:
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, A):
        def _get_ans(A, dp):
            # dp[i]: 以A[i]为结尾的最长子序列长度
            # dp[i] = dp[i - 1] + 1  # if A[i - 1] <= A[i]
            #       = 1              # otherwise
            # init: dp[0] = A[0]
            # ans:  max(dp[0], ..., dp[len(A) - 1])
            ans = dp[0]
            for i in range(1, len(A)):
                if A[i - 1] <= A[i]:
                    dp.append(dp[i - 1] + 1)
                else:
                    dp.append(1)
                ans = max(ans, dp[i])
            return ans

        if not A:
            return 0
        ans = _get_ans(A, [1])
        # reverse in place
        A.reverse()
        return max(ans, _get_ans(A, [1]))
