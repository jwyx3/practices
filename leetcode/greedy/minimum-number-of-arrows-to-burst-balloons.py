# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/discuss/93703/Share-my-explained-Greedy-solution
# keep shooting smallest x_end
# Time: O(nlogn)
# Space: O(1)
# proof using greedy exchange

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # greedy, always point to the smaller end balloon first
        if not points:
            return 0
        points.sort(key=lambda x: (x[1], x[0]))
        res, arrow = 1, points[0][1]
        for i, p in enumerate(points):
            # overlap; use <= because a balloon with xstart and xend
            # bursts by an arrow shot at x if xstart ≤ x ≤ xend
            if p[0] <= arrow:
                continue
            res += 1
            arrow = p[1]
        return res
