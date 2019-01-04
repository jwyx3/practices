# https://leetcode.com/problems/surface-area-of-3d-shapes/
# https://leetcode.com/problems/surface-area-of-3d-shapes/solution/

class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        
        res = 0
        for r in xrange(N):
            for c in xrange(N):
                if grid[r][c]:
                    res += 2
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                        if 0 <= nr < N and 0 <= nc < N:
                            nv = grid[nr][nc]
                        else:
                            nv = 0
                        res += max(grid[r][c] - nv, 0)
        return res
