class Solution:
    #param matrix: a matrix of 0 and 1
    #return: an integer

    # DP
    # dp[i][j]: use (i,j) as left corner, the line length of the largest square containing all 1's
    # row_ones[i][j]: from (i,j) to (i, 0), the number of continuous 1's
    # col_ones[i][j]: from (i,j) to (0, j), the number of continuous 1's
    # dp[i][j] = min(dp[i-1][j-1], row_ones[i][j-1], col_ones[i-1][j]) + 1 # if matrix[i][j] == 1
    #            0 # otherwise
    # row_ones[i][j] = row_ones[i][j-1] + 1  # if matrix[i][j] == 1
    #                = 0                       # otherwise
    # col_ones[i][j] = col_ones[i-1][j] + 1  # if matrix[i][j] == 1
    #                = 0                       # otherwise
    # initial: col_ones[0][j] = matrix[0][j],
    #          row_ones[i][0] = matrix[i][0],
    #          dp[i][0] = matrix[i][0], dp[0][j] = matrix[0][j]
    # n = len(matrix), m = len(matrix[0])
    # ans: max(dp[0][0], ..., dp[n-1][m-1]) ^ 2
    def maxSquare(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        n, m = len(matrix), len(matrix[0])
        row_ones = [[0 for x in range(m)] for y in range(n)]
        col_ones = [[0 for x in range(m)] for y in range(n)]
        dp = [[0 for x in range(m)] for y in range(n)]
        # initial
        for i in range(n):
            row_ones[i][0] = matrix[i][0]
            dp[i][0] = matrix[i][0]
        for j in range(m):
            col_ones[0][j] = matrix[0][j]
            dp[0][j] = matrix[0][j]
        # fill table
        ans = dp[0][0]
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 1:
                    row_ones[i][j] = row_ones[i][j - 1] + 1
                    col_ones[i][j] = col_ones[i - 1][j] + 1
                    dp[i][j] = min(dp[i - 1][j - 1], row_ones[i][j - 1], col_ones[i - 1][j]) + 1
                    ans = max(ans, dp[i][j])
        return ans * ans

