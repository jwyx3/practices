class Solution:
    # @param A: a list of non-negative integers.
    # return: an integer

    # dp[i]: the max count the robber can get with first i houses
    # dp[i] = max(A[i-1] + dp[i-2], dp[i-1])
    # initial: dp[0] = 0, dp[1] = A[0]
    # ans: dp[n]
    def houseRobber(self, A):
        n = len(A)
        if n == 0:
            return 0
        dp = [0, A[0]]
        for i in xrange(2, n + 1):
            dp[i % 2] = max(A[i-1] + dp[(i-2) % 2], dp[(i-1) % 2])
        return dp[n % 2]
