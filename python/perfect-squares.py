class Solution:
    # @param {int} n a positive integer
    # @return {int} an integer

    # dp[i]: min number of perfect square numbers for integer i
    # dp[i]: min{dp[j] + dp[i-j]}, j must be perfect square
    # initial: dp[i] = 1 for all perfect square
    # ans: dp[n]
    def numSquares(self, n):
        if n < 1:
            return 0
        dp = [sys.maxint for _ in range(n + 1)]
        num = 0
        while num * num <= n:
            dp[num * num] = 1
            num += 1
        for i in range(n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i - j * j] + 1, dp[i])
                j += 1
        return dp[n]
