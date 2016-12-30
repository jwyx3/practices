import sys

class Solution:
    # @param {int[]} A an integer array
    # @return {int} an integer

    # 区间类DP
    # dp[i][s]: the min cost to merge stones start from i and the amount is s
    # sums[s]: the sum of s stones start from 0
    # dp[i][s] = sums[i+s] - sums[i] + min(dp[i][s-1]+dp[i+s-1][1],...,dp[i][1] + dp[i+1][s-1])
    # initial: dp[i][1] = 0
    # ans: dp[0][n]
    def stoneGame(self, A):
        if not A or len(A) == 1:
            return 0
        n = len(A)
        sums = [0]
        for s in xrange(1, n+1):
            sums.append(sums[s-1] + A[s-1])
        dp = [[0 if s == 1 else sys.maxint for s in xrange(n+1)] for i in xrange(n)]
        # 大区间依赖小区间
        for s in xrange(2, n+1):
            for i in xrange(n-s+1):
                # 递推式
                for k in xrange(1, s):
                    dp[i][s] = min(dp[i][s], sums[i+s] - sums[i] + dp[i][k] + dp[i+k][s-k])
        return dp[0][n]

