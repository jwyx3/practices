class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    # dp[i][j]: min sum of path until A[i][j]
    # dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + A[i][j] # if j-1>=0 and j<len(A[i-1])
    # initial: dp[0][0] = A[0][0]
    # ans: min(dp[m-1])
    def minimumTotal(self, triangle):
        if not triangle or not triangle[0]:
            return 0
        m = len(triangle)
        dp = [[0 for j in xrange(i + 1)] for i in xrange(m)]
        dp[0][0] = triangle[0][0]
        for i in xrange(1, m):
            n = len(triangle[i])
            for j in xrange(n):
                dp[i][j] = triangle[i][j]
                if j - 1 >= 0 and j < n - 1:
                    dp[i][j] += min(dp[i - 1][j], dp[i - 1][j - 1])
                elif j < 1:
                    dp[i][j] += dp[i - 1][j]
                else:
                    dp[i][j] += dp[i - 1][j - 1]
        return min(dp[m-1])
