# https://leetcode.com/problems/minimum-area-rectangle-ii/
# https://leetcode.com/problems/minimum-area-rectangle-ii/discuss/214704/Python-two-methods%3A-Straightforward-O(N3)-and-Record-center-O(N2-log-N)
# Time: O(N**3)
# Space: O(N)
# find center and radius

class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        points = [complex(*p) for p in points]
        visited = collections.defaultdict(list)
        # combination should give number of elements
        for p, q in itertools.combinations(points, 2):
            center = (p + q) / 2
            radius = abs(center - p)
            # candidates are all nodes share same center and radius
            visited[center, radius].append(p)
        
        res = float('inf')
        for (center, _), candidates in visited.iteritems():
            for p, q in itertools.combinations(candidates, 2):
                # calculate edge and then area
                res = min(res, abs(p - q) * abs(p - (2 * center - q)))
        return res if res < float('inf') else 0
