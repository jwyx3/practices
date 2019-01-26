# https://leetcode.com/problems/line-reflection/
# hints:
# points with min_x and max_x must be reflected
# the line must be (min_x + max_x) / 2
# one point must have one reflected point
# 1) use hash table; Time: O(N); Space: O(N)
# 2) use two pointers - sort x; y should be increasing if it's in left part; and descreasing if it's in right part; Time: O(NlogN), Space: O(1)

# hash set

class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points:
            return True
        
        visited = set()
        min_x = max_x = points[0][0]
        for point in points:
            min_x = min(min_x, point[0])
            max_x = max(max_x, point[0])
            visited.add(tuple(point))
        
        # float!
        mid_x = (min_x + max_x) / 2.0
        
        for x, y in points:
            # this step handle corner cases as well
            if (2 * mid_x - x, y) not in visited:
                return False
        return True

# two pointers + some corner cases!!

class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points:
            return True
        
        min_x = min(x for x, _ in points)
        max_x = max(x for x, _ in points)
        mid_x = (min_x + max_x) / 2.0
        points.sort(key=lambda p: (p[0], p[1] if p[0] <= mid_x else -p[1]))
        
        lo, hi = 0, len(points) - 1
        while lo <= hi:
            # corner case: lo[0] == hi[0] == mid_x
            if (points[lo][0] + points[hi][0]) / 2.0 != mid_x or (
                    points[lo][1] != points[hi][1] and points[lo][0] != points[hi][0]):
                return False
            # handle duplicate and boundary
            while lo <= hi and lo < len(points) - 1 and points[lo + 1] == points[lo]:
                lo += 1
            while lo <= hi and hi > 0 and points[hi - 1] == points[hi]:
                hi -= 1
            lo, hi = lo + 1, hi - 1
        return True
