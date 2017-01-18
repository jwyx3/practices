class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    # dp[i][j]: the min sum of path to A[i][j]
    # dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + A[i][j]
    # initial: dp[0][j] = dp[0][j-1] + A[0][j]
    #          dp[i][0] = dp[i-1][0] + A[i][0]
    # ans: dp[m-1][n-1]
    def minPathSum(self, grid):
        # write your code here
        if not grid and not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0 for j in xrange(n)] for i in xrange(2)]
        dp[0][0] = grid[0][0]
        for j in xrange(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        col1 = [0 for i in xrange(m)]
        col1[0] = grid[0][0]
        for i in xrange(1, m):
            col1[i] = col1[i - 1] + grid[i][0]

        for i in xrange(1, m):
            dp[i % 2][0] = col1[i]
            for j in xrange(1, n):
                dp[i % 2][j] = min(dp[(i - 1) % 2][j], dp[i % 2][j - 1]) + grid[i][j]
        return dp[(m - 1) % 2][n - 1]
