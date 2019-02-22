# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/
# Time: O(N*M)
# Space: O(N*M)

class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        # N = len(s1), M = len(s2)
        # dp[i][j]: the lowest sum of deleted characters to make s1[i:] and s2[j:] equal
        # dp[i][j] = min(s1[i] + dp[i+1][j], s2[j] + dp[i][j+1]), if s1[i] != s2[j]
        #          = dp[i+1][j+1], if s1[i] == s2[j]
        # initial: dp[i][M] = sum(s1[i:]), dp[N][j] = sum(s2[j:])
        # answer: dp[0][0]
        N, M = len(s1), len(s2)
        dp = [[0] * (M + 1) for _ in xrange(N + 1)]
        for i in xrange(N-1, -1, -1):
            dp[i][M] = dp[i+1][M] + ord(s1[i])
        for j in xrange(M-1, -1, -1):
            dp[N][j] = dp[N][j+1] + ord(s2[j])
        for i in xrange(N-1, -1, -1):
            for j in xrange(M-1, -1, -1):
                if s1[i] != s2[j]:
                    dp[i][j] = min(ord(s1[i]) + dp[i+1][j], ord(s2[j]) + dp[i][j+1])
                else:
                    dp[i][j] = dp[i+1][j+1]
        return dp[0][0]
            
