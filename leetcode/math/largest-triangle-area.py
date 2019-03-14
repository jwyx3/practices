# https://leetcode.com/problems/largest-triangle-area/
# https://leetcode.com/problems/largest-triangle-area/solution/
# https://leetcode.com/problems/largest-triangle-area/discuss/122711/C%2B%2BJavaPython-Solution-with-Explanation-and-Prove
# Time: O(N**3)
# Space: O(1)

class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def area(p, q, r):
            return 0.5 * abs(p[0]*q[1] + q[0]*r[1] + r[0]*p[1] - p[1]*q[0] - q[1]*r[0] - r[1]*p[0])
        
        return max(area(p, q, r) for p, q, r in itertools.combinations(points, 3))
