# https://leetcode.com/problems/max-increase-to-keep-city-skyline/
# Time: O(N*N)
# Space: O(N)

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R, C = len(grid), len(grid[0])
        mrows = [max(cols) for cols in grid]
        mcols = [max(grid[r][c] for r in xrange(R)) for c in xrange(C)]
        res = 0
        for r in xrange(R):
            for c in xrange(C):
                res += max(0, min(mrows[r], mcols[c]) - grid[r][c])
        return res
