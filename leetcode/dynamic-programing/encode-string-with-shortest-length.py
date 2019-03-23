# https://leetcode.com/problems/encode-string-with-shortest-length/
# http://www.cnblogs.com/grandyang/p/6194403.html
# Time: O(N**3)
# Space: O(N**2)

class Solution(object):
    def encode(self, s):
        """
        :type s: str
        :rtype: str
        """
        # dp(i, j): the shortest encoded string for s[i:j+1]
        # dp(i, j) = min{
        #              min{dp(i,k) + dp(k+1,j)},  # i<=k<j
        #              repeat  # if s[i:j+1] has repeat pattern
        #            }
        # initial: dp(i,j) = s[i:j+1], if j-i+1<=4
        # answer: dp(0,len(s)-1)
        n = len(s)
        dp = [[None] * n for _ in xrange(n)]

        for l in xrange(1, n + 1):
            for i in xrange(n - l + 1):
                j = i + l - 1
                dp[i][j] = s1 = s[i:j+1]
                s2 = s1 * 2
                k = s2.find(s1, 1)
                if k > 0 and k < len(s1):  # if repeat pattern is found
                    repeat = "{}[{}]".format(len(s1) / k, dp[i][i+k-1])
                    if len(repeat) < len(dp[i][j]):
                        dp[i][j] = repeat
                else:
                    for k in xrange(i, j):
                        if len(dp[i][j]) > len(dp[i][k]) + len(dp[k+1][j]):
                            dp[i][j] = dp[i][k] + dp[k+1][j]
        return dp[0][n-1]
