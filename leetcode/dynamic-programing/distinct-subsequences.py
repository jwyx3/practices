# https://leetcode.com/problems/distinct-subsequences/
# Time: O(N * M)
# Space: O(M)

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # dp[i][j]: count the number of distinct subsequences of s[:i] which equals t[:j]
        # initial: dp[i][0] = 1, dp[0][j>0] = 0
        # dp[i][j] = dp[i-1][j-1] + dp[i-1][j], if s[i-1] == t[j-1]
        #          = dp[i-1][j], otherwise
        # answer: dp[N][M]
        # -> 1D
        N, M = len(s), len(t)
        dp = [0] * (M + 1)
        dp[0] = 1
        for i in xrange(1, N + 1):
            for j in xrange(M, 0, -1):
                if s[i-1] == t[j-1]:
                    dp[j] += dp[j-1]
                else:
                    dp[j] = dp[j]
        return dp[M]

