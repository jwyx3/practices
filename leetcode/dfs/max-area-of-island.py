class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        visited = set()
        # from x,y find the size of island
        def dfs(x, y):
            if not (0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in visited and grid[x][y]):
                return 0
            visited.add((x,y))
            return 1 + dfs(x+1,y) + dfs(x-1,y) + dfs(x,y-1) + dfs(x,y+1)

        result = 0
        for x in xrange(len(grid)):
            for y in xrange(len(grid[0])):
                if grid[x][y] and (x, y) not in visited:
                    result = max(result, dfs(x, y))
        return result
