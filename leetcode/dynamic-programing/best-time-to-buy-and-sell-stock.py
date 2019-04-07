# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Time: O(n)
# Space: O(1)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        ans, min_price = 0, prices[0]
        for price in prices:
            ans = max(ans, price - min_price)
            min_price = min(min_price, price)
        return ans
        
