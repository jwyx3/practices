# https://leetcode.com/problems/interleaving-string/
# https://leetcode.com/problems/interleaving-string/solution/
# Time: O(N*M)
# Space: O(M)

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # dp[i][j]: find whether s3 is formed by the interleaving of s1[:i] and s2[:j]
        #           0<=i<=len(s1), 0<=j<=len(s2)
        # dp[i][j]  = True, i==0 and j==0
        #          = dp[i-1][j] and s1[i-1] == s3[i+j-1], j==0
        #          = dp[i][j-1] and s2[j-1] == s3[i+j-1], i==0
        #          = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        # answer: dp[N][M]
        # -> con
        N, M = len(s1), len(s2)
        if N + M != len(s3):
            return False
        if N < M:
            s1, s2 = s2, s1
        N, M = len(s1), len(s2)
        dp = [False] * (M + 1)
        for i in xrange(N + 1):
            for j in xrange(M + 1):
                if i == 0 and j == 0:
                    dp[j] = True
                elif i == 0:
                    dp[j] = dp[j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0:
                    dp[j] = dp[j] and s1[i-1] == s3[i+j-1]
                else:
                    dp[j] = (dp[j-1] and s2[j-1] == s3[i+j-1]) or (dp[j] and s1[i-1] == s3[i+j-1])
        return dp[M]
