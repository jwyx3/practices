# https://leetcode.com/problems/projection-area-of-3d-shapes/
# https://leetcode.com/problems/projection-area-of-3d-shapes/solution/
# Time: O(N**2)
# Space: O(1)

class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        n = len(grid)
        ans = 0
        for i in xrange(n):
            best_row = best_col = 0
            for j in xrange(n):
                if grid[i][j]:
                    ans += 1
                best_row = max(best_row, grid[i][j])
                best_col = max(best_col, grid[j][i])
            ans += best_row + best_col
        return ans
