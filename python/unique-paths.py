class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """
    # dp[i][j]: max number of unique paths to reach i,j
    # dp[i][j] = dp[i-1][j] + dp[i][j-1]
    # initial: dp[0][j] = 1, dp[i][0] = 1
    # ans: dp[m-1][n-1]
    def uniquePaths(self, m, n):
        # write your code here
        dp = [[1 for j in xrange(n)] for i in xrange(2)]
        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[i % 2][j] = dp[(i - 1) % 2][j] + dp[i % 2][j - 1]
        return dp[(m - 1) % 2][n - 1]
