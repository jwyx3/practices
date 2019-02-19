# https://leetcode.com/problems/minimum-number-of-refueling-stops/
# https://leetcode.com/problems/minimum-number-of-refueling-stops/solution/
# https://www.youtube.com/watch?v=vWTPA5zw24M
# dp[i]: the farthest location we can get to using i refueling stops.
# we want the smallest i for which dp[i] >= target.
# 区别于一般的dp，问题的定义：结果不是dp的值，而是dp的参数。
# 参考0-1背包问题
# for each station, either stop or not.

class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        # dp[t]: the farthest location we can get to using t refueling stops.
        N = len(stations)
        dp = [0] * (N + 1)
        dp[0] = startFuel
        
        # if we add one station one by one
        for i, (pos, gas) in enumerate(stations):
            # to use 1d array, from high to low
            for t in xrange(i, -1, -1):
                if dp[t] >= pos:
                    dp[t+1] = max(dp[t+1], dp[t] + gas)
        for t in xrange(N+1):
            if dp[t] >= target:
                return t
        return -1

# can use greedy. refer to greedy/minimum-number-of-refueling-stops.py
