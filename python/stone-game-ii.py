import sys

class Solution:
    # @param {int[]} A an integer array
    # @return {int} an integer

    # 扩展成2n, 化环为链
    # dp[i][s]: the min cost to merge stones (start from i and the amount is s)
    # sums[s]: the sum of first s stones
    # dp[i][s] = sums[i+s] - sums[i] + min(dp[i][1] + dp[i+1][s-1],...,dp[i][s-1] + dp[i+s-1][1])
    # initial: dp[i][1] = 0
    # ans: dp[i][n], 0 <= i < n
    def stoneGame2(self, A):
        if not A or len(A) == 1:
            return 0
        n = len(A)
        sums = [0]
        for s in xrange(1, 2*n+1):
            # A 用取模的形式扩展
            sums.append(sums[s-1] + A[(s-1) % n])
        dp = [[0 if s == 1 else sys.maxint for s in xrange(n+1)] for i in xrange(2*n)]
        for s in xrange(2, n+1):
            for i in xrange(2*n-s+1):
                for k in xrange(1, s):
                    dp[i][s] = min(dp[i][s], dp[i][k] + dp[i+k][s-k])
                dp[i][s] += (sums[i+s] - sums[i])
        # 计算答案
        ans = sys.maxint
        for i in xrange(n):
            ans = min(ans, dp[i][n])
        return ans

