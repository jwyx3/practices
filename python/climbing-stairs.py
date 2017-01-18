class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    # dp[i]: In how many distinct ways can you climb to the top (i steps)
    # dp[i] = dp[i-1] + dp[i-2]
    # initial: dp[0] = 1, dp[1] = 1
    # ans: dp[n]
    def climbStairs(self, n):
        dp = [1, 1]
        for i in xrange(2, n + 1):
            dp[i % 2] = dp[(i - 1) % 2] + dp[(i - 2) % 2]
        return dp[n % 2]
