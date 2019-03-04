# https://leetcode.com/problems/scramble-string/
# http://www.cnblogs.com/grandyang/p/4318500.html
# Time: O(N**4)
# Space: O(N**3)

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # dp[l][i][j]: determine if s2[j:j+l] is a scrambled string of s1[i:i+l]
        # dp[l][i][j] |= (dp[k][i][j] and dp[l-k][i+k][j+k])
        #                or (dp[k][i][j+l-k] and dp[l-k][i+k][j]), k=1..l-1
        # initial: dp[1][i][j] = s1[i] == s2[j], otherwise false
        # answer: dp[n][0][0]
        if not s1 and not s2:
            return True
        if not s1 or not s2 or len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        n = len(s1)
        dp = [[[False] * n for _ in xrange(n)] for _ in xrange(n + 1)]
        for i in xrange(n):
            for j in xrange(n):
                dp[1][i][j] = s1[i] == s2[j]
        for l in xrange(2, n + 1):
            for i in xrange(n - l + 1):
                for j in xrange(n - l + 1):
                    for k in xrange(1, l):
                        dp[l][i][j] |= ((dp[k][i][j] and dp[l-k][i+k][j+k]) or
                                       (dp[k][i][j+l-k] and dp[l-k][i+k][j]))
                        if dp[l][i][j]:
                            break
        return dp[n][0][0]
