class Solution:
    # @param word1 & word2: Two string.
    # @return: The minimum number of steps.
    # dp[i][j] = min number of steps required to convert word1 (len i)
    #            to word2 (len j)
    # dp[i][j] = dp[i-1][j-1] # if word1[i-1] == word2[j-1]
    #            min(
    #            dp[i][j-1] + 1   # if insert a character into word1
    #            dp[i-1][j] + 1   # if delete a character into word1
    #            dp[i-1][j-1] + 1 # if replace a character
    #            )
    # initial: dp[0][j] = j, dp[i][0] = i
    # ans: dp[len(word1)][len(word2)]
    def minDistance(self, word1, word2):
        # write your code here
        if word1 is None or word2 is None:
            return 0
        m, n = len(word1), len(word2)
        dp = [[0 for j in xrange(n + 1)] for i in xrange(2)]
        for j in xrange(n + 1):
            dp[0][j] = j
        for i in xrange(1, m + 1):
            dp[i % 2][0] = i
            for j in xrange(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i % 2][j] = dp[(i - 1) % 2][j-1]
                else:
                    dp[i % 2][j] = min(
                        dp[i % 2][j-1],
                        dp[(i - 1) % 2][j],
                        dp[(i - 1) % 2][j-1]
                    ) + 1
        return dp[m % 2][n]
