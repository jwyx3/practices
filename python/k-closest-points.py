# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __repr__(self):
        return "[{},{}]".format(self.x, self.y)


from heapq import heappush, heappop
import math


class Solution:
    # @param {Pint[]} points a list of points
    # @param {Point} origin a point
    # @param {int} k an integer
    # @return {Pint[]} the k closest points
    def kClosest(self, points, origin, k):
        # Write your code here
        if not points or k <= 0:
            return []
        h = [] # max heap
        for point in points:
            heappush(h, ((-self.getDistance(point, origin), -point.x, -point.y), point))
            if len(h) > k:
                heappop(h)
        ans = []
        while len(h) > 0:
            curt = heappop(h)
            ans.insert(0, curt[1])
        return ans

    def getDistance(self, start, end):
        return math.sqrt((start.x - end.x) ** 2 + (start.y - end.y) ** 2)


if __name__ == '__main__':
    s = Solution()
    print s.kClosest([Point(4,6), Point(4,7), Point(4,4), Point(2,5), Point(1,1)], Point(0,0), 3)
