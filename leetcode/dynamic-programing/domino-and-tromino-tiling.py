# https://leetcode.com/problems/domino-and-tromino-tiling/
# Time: O(N)
# Space: O(1)

class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        # dp[i][shape]: cover 2*i board ending with shape
        # shapes: 0, 1
        # X  X   
        # X,   or X
        # 0  1
        # dp[i][0] = dp[i-1][0] + dp[i-2][0] + dp[i-1][1]
        # dp[i][1] = 2*dp[i-2][0] + dp[i-1][1]
        # initial: dp[0][0] = 0, dp[1][0] = 1, dp[2][0] = 2
        #          dp[0][1] = 0, dp[1][1] = 0, dp[2][1] = 2
        # answer: dp[N][0]
        MOD = 10 ** 9 + 7
        dp = [[0, 0] for _ in xrange(3)]
        dp[1][0] = 1
        dp[2][0] = 2
        dp[2][1] = 2
        for i in xrange(3, N + 1):
            dp[i%3][0] = (dp[(i-1)%3][0] + dp[(i-2)%3][0] + dp[(i-1)%3][1]) % MOD
            dp[i%3][1] = (2 * dp[(i-2)%3][0] + dp[(i-1)%3][1]) % MOD
        return dp[N%3][0]
