# https://leetcode.com/problems/minimize-max-distance-to-gas-station

class Solution(object):
    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        # binary search on answers
        if not stations or K < 0:
            return 0.0
        start = end = 0
        for i in xrange(1, len(stations)):
            end = max(end, stations[i] - stations[i-1])
        E = 1e-6
        while end - start > E:
            mid = (start + end) / 2.0
            if self.check(stations, mid, K):
                end = mid
            else:
                start = mid
        return start
    
    def check(self, stations, mid, K):
        count = 0
        for i in xrange(1, len(stations)):
            d = stations[i] - stations[i - 1]
            # d/mid is amount of partitions. so we need d/mid - 1 station.
            count += math.ceil(d / mid) - 1
            if count > K:
                return False
        return True
            
