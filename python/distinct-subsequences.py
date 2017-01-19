class Solution:
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    # dp[i][j]: the number of distinct subsequences for S (len i), T (len j)
    # dp[i][j] = dp[i-1][j] + dp[i-1][j-1] # if S[i-1] == T[i-1], we can choose to S[-1]
    #            dp[i-1][j]  # otherwise, have to remove S[-1]
    # initial: dp[i][0] = 1  # S can remove all character to get T, dp[0][j] = 0
    # ans: dp[m][n]
    def numDistinct(self, S, T):
        # write your code here
        if S is None or T is None:
            return 0
        m, n = len(S), len(T)
        dp = [[0 for j in xrange(n + 1)] for i in xrange(m + 1)]
        for i in xrange(m + 1):
            dp[i][0] = 1
        for j in xrange(1, n + 1):
            dp[0][j] = 0
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if S[i - 1] == T[j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[m][n]
