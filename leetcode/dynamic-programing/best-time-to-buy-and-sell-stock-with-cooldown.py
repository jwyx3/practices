# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75931/Easiest-JAVA-solution-with-explanations
# Time: O(n)
# Space: O(1)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # buy[i]: max profit until day i. last transaction is buy
        # sell[i]: max profit until day i. last transaction is sell.
        # 1. either buy before/at day i-1 and do nothing. or sell before/at day i-2 and buy at i
        # buy[i] = max(buy[i-1], sell[i-2] - prices[i])
        # 2. either sell before/at day i-1 and do nothing. or buy before/at day i-1 and sell at i
        # sell[i] = max(sell[i-1], buy[i-1] + prices[i])
        # initial: buy[0] = -prices[0], sell[0] = 0
        # answer: sell[N-1]
        if not prices or len(prices) == 1:
            return 0
        N = len(prices)
        buy = [0] * 3
        sell = [0] * 3
        buy[0] = -prices[0]
        for i in xrange(1, N):
            buy[i%3] = max(buy[(i-1)%3], sell[(i-2)%3] - prices[i])
            sell[i%3] = max(sell[(i-1)%3], buy[(i-1)%3] + prices[i])
        return sell[(N-1)%3]
