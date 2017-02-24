class Solution:
    # @param {int} n an integer
    # @return {int} an integer

    # dp[i]: number of ways to represent i cents
    # dp[i] = sum{dp[i - cent]} # cent = 1, 5, 10, 25 and i - cent >= 0
    # initial: dp[0] = 1
    # answer: dp[n]
    def waysNCents(self, n):
        # Write your code here
        if n < 0:
            return -1
        cents = [1, 5, 10, 25]
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        for cent in cents:
            for i in range(cent, n + 1):
                dp[i] += dp[i - cent]
        return dp[n]
