# https://leetcode.com/problems/online-stock-span/
# Time: O(N)
# Space: O(N)
# keep desending stack and save both index and price

class StockSpanner(object):

    def __init__(self):
        self.idx = 1
        self.stack = [(float('inf'), 0)]

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        res = self.idx  - self.stack[-1][1]
        self.stack.append((price, self.idx))
        self.idx += 1
        return res
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
