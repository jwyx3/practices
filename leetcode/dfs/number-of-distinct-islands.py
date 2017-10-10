class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0

        def dfs(x0, y0, x, y):
            if not (0 <= x < len(grid) and 0 <= y <len(grid[0]) and grid[x][y] == 1):
                return []
            grid[x][y] = -1
            return [(x-x0,y-y0)] + dfs(x0,y0,x+1,y) + dfs(x0,y0,x-1,y) + dfs(x0,y0,x,y+1) + dfs(x0,y0,x,y-1)

        for x in xrange(len(grid)):
            for y in xrange(len(grid[0])):
                if grid[x][y] == 1:
                    islands.add(''.join(str(n) for n in sorted(dfs(x,y,x,y))))
        # still keep 2-d for encoding
        islands = set()
        return len(islands)
