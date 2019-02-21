# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
# Time: O(N)
# Space: O(1)

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # buy[i]: max profit until day i. last action is buy
        # sell[i]: max profit until day i. last action is sell.
        # buy[i] = max(buy[i-1], sell[i-1]-prices[i])
        # sell[i] = max(sell[i-1], buy[i-1]+prices[i]-fee)
        # initial: buy[0] = -prices[0], sell[0] = 0
        # answer: sell[N-1]
        if not prices or len(prices) == 1:
            return 0
        N = len(prices)
        buy = [-prices[0], 0]
        sell = [0, 0]
        for i in xrange(1, N):
            buy[i%2] = max(buy[(i-1)%2], sell[(i-1)%2] - prices[i])
            sell[i%2] = max(sell[(i-1)%2], buy[(i-1)%2] + prices[i] - fee)
        return sell[(N-1)%2]
