# https://leetcode.com/problems/divisor-game/
# Time: O(n*n)
# Space: O(n)

class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        # dp[i] = current user can win for number i
        # dp[i] = any(not dp[i-x]), 0 < x < N and N % x == 0
        # Initial: dp[1] = False
        # Answer: dp[N]
        dp = [False] * (N + 1)
        for i in xrange(2, N + 1):
            dp[i] = any(not dp[i-x] for x in xrange(1, i) if i % x == 0)
        return dp[N]
                    

# better to use math!!
# https://leetcode.com/problems/divisor-game/discuss/274606/JavaC%2B%2BPython-return-N-2-0

class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        return N % 2 == 0
