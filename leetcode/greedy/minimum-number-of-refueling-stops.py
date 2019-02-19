# https://leetcode.com/problems/minimum-number-of-refueling-stops/
# https://leetcode.com/problems/minimum-number-of-refueling-stops/solution/
# Time: O(nlogn)
# Space: O(n)

class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        # fuel until tank is not enough
        tank = startFuel
        res = prev = 0
        stations.append((target, 0))
        h = []
        for pos, gas in stations:
            tank -= pos - prev
            while h and tank < 0:
                tank -= heapq.heappop(h)
                res += 1
            if tank < 0:
                return -1
            heapq.heappush(h, -gas)
            prev = pos
        return res
