class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    # dp[i][j]: max unique paths to reach i,j
    # dp[i][j] = dp[i-1][j] + dp[i][j-1] # if A[i][j] == 0
    #          = 0                       # otherwise
    # initial:  dp[0][j] = 1 # before first A[0][j] == 1
    #                    = 0 # otherwise
    #           dp[i][0] = 1 # before first A[i][0] == 1
    #                    = 0 # otherwise
    # ans: dp[m-1][n-1]
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        first_col_dp = [0 for i in xrange(m)]
        dp = [[0 for j in xrange(n)] for i in xrange(2)]

        for j in xrange(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1

        for i in xrange(m):
            if obstacleGrid[i][0] == 1:
                break
            first_col_dp[i] = 1

        for i in xrange(1, m):
            dp[i % 2][0] = first_col_dp[i]
            for j in xrange(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i % 2][j] = 0
                else:
                    dp[i % 2][j] = dp[(i - 1) % 2][j] + dp[i % 2][j - 1]
        return dp[(m - 1) % 2][n - 1]


