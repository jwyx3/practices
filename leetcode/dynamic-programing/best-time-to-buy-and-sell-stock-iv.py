# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
# Time: O(N*K)
# Space: O(N)
class Solution(object):
    def maxProfit(self, K, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # dp[k][i]: max profit until day i at most k transactions
        # dp[k][i] = max(dp[k][i-1], max(prices[i] - prices[j] + dp[k-1][j])), j < i
        #          = max(dp[k][i-1], prices[i] + max(dp[k-1][j] - prices[j])), j < i
        # initial: dp[0][i] = 0, dp[k][0] = 0
        # answer: dp[K][N-1]
        if not prices or len(prices) == 1:
            return 0
        N = len(prices)
        if K >= N / 2:
            return sum(prices[i+1] - prices[i] for i in xrange(N - 1) if prices[i+1] > prices[i])
        dp = [[0] * N for _ in xrange(2)]
        for k in xrange(1, K+1):
            m = dp[(k-1)%2][0] - prices[0]
            for i in xrange(1, N):
                dp[k%2][i] = max(dp[k%2][i-1], prices[i] + m)
                m = max(m, dp[(k-1)%2][i] - prices[i])
        return dp[K%2][N-1]

# better space: O(K)
class Solution(object):
    def maxProfit(self, K, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        N = len(prices)
        # corner case!!
        if K >= N / 2:  # we can get all profit
            return sum(prices[i+1] - prices[i] for i in xrange(N - 1) if prices[i+1] > prices[i])
        # buy[i][k]: max profit at most k transactions, last transaction is buy
        # sell[i][k]: max profit at most k transactions, last transaction is sell
        # buy[i][k] = max(buy[i-1][k], sell[i-1][k-1] - prices[i])
        # sell[i][k] = max(sell[i-1][k], buy[i][k] + prices[i])
        # initial: buy[0][*] = -prices[0]
        # answer: sell[N-1][K]
        buy = [-prices[0]] * (K + 1)
        sell = [0] * (K + 1)
        for i in xrange(1, N):
            for k in xrange(1, K + 1):
                buy[k] = max(buy[k], sell[k-1] - prices[i])
                sell[k] = max(sell[k], buy[k] + prices[i])
        return sell[K]
