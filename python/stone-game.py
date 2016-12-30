import sys

class Solution:
    # @param {int[]} A an integer array
    # @return {int} an integer

    # 区间类DP
    # dp[i][k]: the min cost to merge stones start from i and the amount is k
    # sums[k]: the sum of k stones start from 0
    # dp[i][k] = sums[i+k] - sums[i] + min(dp[i][k-1]+dp[i+k-1][1],...,dp[i][1] + dp[i+1][k-1])
    # initial: dp[i][1] = 0
    # ans: dp[0][n]
    def stoneGame(self, A):
        if not A or len(A) == 1:
            return 0
        n = len(A)
        sums = [0]
        for k in xrange(1, n+1):
            sums.append(sums[k-1] + A[k-1])
        dp = [[0 if k == 1 else sys.maxint for k in xrange(n+1)] for i in xrange(n)]
        # 大区间依赖小区间
        for k in xrange(2, n+1):
            for i in xrange(n-k+1):
                # 递推式
                for j in xrange(1, k):
                    dp[i][k] = min(dp[i][k], sums[i+k] - sums[i] + dp[i][j] + dp[i+j][k-j])
        return dp[0][n]

