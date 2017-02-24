class Solution:
    """
    @param {int} n a integer
    @return {int} a integer
    """
    # dp[i]: possible ways the child can run up to ith stair
    # dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3], if i - n is not out of index
    # initial: dp[0] = 1
    # answer: dp[n]
    def climbStairs2(self, n):
        # Write your code here
        if n < 0:
            return 0
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            if i - 2 >= 0:
                dp[i] += dp[i - 2]
            if i - 3 >= 0:
                dp[i] += dp[i - 3]
        return dp[n]
