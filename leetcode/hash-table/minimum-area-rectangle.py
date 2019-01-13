# https://leetcode.com/problems/minimum-area-rectangle/
# https://leetcode.com/problems/minimum-area-rectangle/solution/
# learn the way to determine rectangle
# Time: O(n*n)
# Space: O(n)

class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        seen = set(tuple(x) for x in points)
        res = float('inf')
        # find diagonal and check rectangle
        # use hash table because we need to check existence
        for i in xrange(len(points)):
            for j in xrange(i):
                p1, p2 = points[i], points[j]
                if p1[0] != p2[0] and p1[1] != p2[1] and\
                        (p1[0], p2[1]) in seen and (p2[0], p1[1]) in seen:
                    res = min(res, abs(p1[0] - p2[0]) * abs(p1[1] - p2[1]))
        return res if res < float('inf') else 0
