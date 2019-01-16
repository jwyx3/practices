# https://leetcode.com/problems/coin-change-2/
# Time: O(N * amount)
# Space: O(amount)

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # dp[i][j]: the number of combinations for amount j and first i coins
        # dp[i][j] = sum{dp[i-1][j + k * coins[i-1]]}, 0<=k<=j/coins[i-1]
        # initial: dp[0][0] = 1, dp[0][>0] = 0
        # answer: dp[len(coins)][amount]
        
        N = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for i in xrange(1, N + 1):
            for j in xrange(amount, -1, -1):
                # start from 1 becuase dp[j] is k == 0 case
                for k in xrange(1, j/coins[i-1]+1):
                    dp[j] += dp[j-k*coins[i-1]]
        return dp[amount]
