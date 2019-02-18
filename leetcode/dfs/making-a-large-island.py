# https://leetcode.com/problems/making-a-large-island/
# https://leetcode.com/problems/making-a-large-island/solution/
# Time: O(N**2)
# Space: O(N**2)

class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        
        def neighbor(r, c):
            for nr, nc in ((r+1, c), (r-1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < N and 0 <= nc < N:
                    yield nr, nc
        
        # find group and return size of this group
        def dfs(r, c, gid):
            res = 1
            grid[r][c] = gid
            for nr, nc in neighbor(r, c):
                if grid[nr][nc] == 1:
                    res += dfs(nr, nc, gid)
            return res
        
        gid = 2
        groups = {}
        for r in xrange(N):
            for c in xrange(N):
                if grid[r][c] == 1:
                    groups[gid] = dfs(r, c, gid)
                    gid += 1

        # corner case: no 1 in grid
        res = max(groups.itervalues()) if groups else 0        
        for r in xrange(N):
            for c in xrange(N):
                if grid[r][c] == 0:
                    # find groups nearby
                    ids = set(grid[nr][nc] for nr, nc in neighbor(r, c) if grid[nr][nc] > 1)
                    res = max(res, 1 + sum(groups[i] for i in ids))
        return res
