class Solution:
    # @param n: an integer
    # @return: a boolean which equals to True if the first player will win

    # dp[i]: current player win with i stones
    def firstWillWin(self, n):
        if n == 0:
            return False
        if n <= 2:
            return True
        dp = [False, True, True]
        for i in xrange(3, n + 1):
            dp[i % 3] = not (dp[(i - 1) % 3] and dp[(i - 2) % 3])
        return dp[n % 3]

