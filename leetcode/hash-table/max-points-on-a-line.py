# https://leetcode.com/problems/max-points-on-a-line/
# https://leetcode.com/problems/max-points-on-a-line/solution/
# Time: O(N**2)
# Space: O(N)
# duplicate, count, horizontal_lines, lines[scope]

# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        n = len(points)
        
        def max_points_via_point(i):
            lines, horizontal_lines = {}, 1
            count, duplicates = 1, 0
            x1 = points[i].x
            y1 = points[i].y
            for j in xrange(i + 1, n):
                x2 = points[j].x
                y2 = points[j].y
                if x1 == x2 and y1 == y2:
                    duplicates += 1
                elif y1 == y2:
                    horizontal_lines += 1
                    count = max(count, horizontal_lines)
                else:
                    # scope defined as 1/scope to handle x1==x2
                    # use float divide
                    scope = 1.0 * (x1 - x2) / (y1 - y2)                        
                    lines[scope] = lines.get(scope, 1) + 1
                    count = max(count, lines[scope])
            return count + duplicates

        # corner case. e.g. [], [[0, 0]]
        ans = 0
        for i in xrange(n):
            ans = max(ans, max_points_via_point(i))
        return ans

