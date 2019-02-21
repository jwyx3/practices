# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39608/A-clean-DP-solution-which-generalizes-to-k-transactions
# Time: O(N)
# Space: O(N)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        N = len(prices)
        # dp1[i]: max profit for day [0, i].
        # dp2[i]: max profit during day [i, N-1].
        dp1 = [0] * N
        dp2 = [0] * N
        
        # m: min price from day 0..i-1
        m = float('inf')
        for i in xrange(N):
            if i > 0:
                dp1[i] = max(dp1[i - 1], prices[i] - m)
            m = min(m, prices[i])
        # m: max price from day N-1..i+1
        m = 0
        for i in xrange(N-1, -1, -1):
            if i < N - 1:
                dp2[i] = max(dp2[i + 1], m - prices[i])
            m = max(m, prices[i])
        # at most 1 transaction
        res = max(dp1)
        # two transactions
        for i in xrange(N - 1):
            res = max(res, dp1[i] + dp2[i+1])
        return res

# use at most k transactions
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        
        N = len(prices)
        # dp[k][i]: max profit until day i (not sell at day i) at most k transaction
        # dp[k][i] = max(dp[k][i-1], max(prices[i] - prices[j] + dp[k-1][j]))
        #            max(dp[k][i-1], prices[i] + max(dp[k-1][j] - prices[j])), j < i
        # initial: dp[0][i] = 0, dp[k][0] = 0
        # answer: dp[2][N-1]
        dp = [[0] * N for _ in xrange(3)]
        for k in xrange(1, 3):
            m = dp[k-1][0] - prices[0]
            for i in xrange(1, N):
                dp[k][i] = max(dp[k][i-1], prices[i] + m)
                m = max(m, dp[k-1][i] - prices[i])
        return dp[2][N-1]

# use space O(1)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        
        N = len(prices)
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0
        for i in xrange(1, N):
            # at most 1 transaction
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            # at most 2 transaction
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2
