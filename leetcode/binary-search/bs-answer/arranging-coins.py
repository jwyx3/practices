# 二分答案看是否能找到总数<n的最大答案
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 0, n
        while start + 1 < end:
            mid = (start + end) / 2
            total = self.get_total(mid)
            if total <= n:
                start = mid
            else:
                end = mid - 1
        if self.get_total(end) <= n:
            return end
        return start

    def get_total(self, x):
        return (1 + x) * x / 2
