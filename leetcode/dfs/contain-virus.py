# https://leetcode.com/problems/contain-virus/
# http://www.cnblogs.com/grandyang/p/8424780.html
# http://zxi.mytechroad.com/blog/searching/leetcode-749-contain-virus/
# Time: O(M*N*(M+N)), each day takes O(M*N) and O(M+N) days
# Space: O(M*N)
# 136 ms

class Solution(object):
    def containVirus(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # walls are only built on the shared boundary of two different cells
        # (num of cells, list of virus, list of walls)
        # state: (x << 8) | y
        h, ans = [], 0
        m, n = len(grid), len(grid[0])
        
        def dfs(x, y, walls, virus):
            for nx, ny in ((x-1, y), (x+1, y), (x, y+1), (x, y-1)):
                if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] < 0:
                    continue
                if grid[nx][ny] == 0:
                    walls.append((nx << 8) | ny)
                else:
                    grid[nx][ny] = -1
                    virus.append((nx << 8) | ny)
                    dfs(nx, ny, walls, virus)
        
        def candidates():
            cands, max_cells, max_i = [], 0, 0
            for x in xrange(m):
                for y in xrange(n):
                    if grid[x][y] == 1:
                        grid[x][y] = -1
                        # add x, y into virus
                        walls, virus = [], [(x << 8) | y]
                        dfs(x, y, walls, virus)
                        cells = len(set(walls))
                        if cells:  # not more cells
                            if cells > max_cells:
                                max_i, max_cells = len(cands), cells
                            cands.append((cells, virus, walls))
            return cands, max_i

        ans, (q, max_i) = 0, candidates()
        while q:
            _, _, walls = q[max_i]
            ans += len(walls)
            # rollback infected cells
            for i, (_, virus, walls) in enumerate(q):
                if i == max_i:
                    continue
                for state in itertools.chain(virus, walls):
                    x, y = state >> 8, state & 0xff
                    grid[x][y] = 1
            q, max_i = candidates()
        return ans

# better runtime. but worse O() time
# 72 ms

class Solution(object):
    def containVirus(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # walls are only built on the shared boundary of two different cells
        # use heap for (num of cells, list of virus, list of walls)
        # state: (x << 8) | y
        h, ans = [], 0
        m, n = len(grid), len(grid[0])
        
        def dfs(x, y, walls, virus):
            for nx, ny in ((x-1, y), (x+1, y), (x, y+1), (x, y-1)):
                if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] < 0:
                    continue
                if grid[nx][ny] == 0:
                    walls.append((nx << 8) | ny)
                else:
                    grid[nx][ny] = -1
                    virus.append((nx << 8) | ny)
                    dfs(nx, ny, walls, virus)
        
        def candidates():
            h = []
            for x in xrange(m):
                for y in xrange(n):
                    if grid[x][y] == 1:
                        grid[x][y] = -1
                        # add x, y into virus
                        walls, virus = [], [(x << 8) | y]
                        dfs(x, y, walls, virus)
                        cells = len(set(walls))
                        if cells:  # not more cells
                            heapq.heappush(h, (-cells, virus, walls))
            return h

        ans, h = 0, candidates()
        while h:
            _, _, walls = heapq.heappop(h)
            ans += len(walls)
            # rollback infected cells
            for _, virus, walls in h:
                for state in itertools.chain(virus, walls):
                    x, y = state >> 8, state & 0xff
                    grid[x][y] = 1
            h = candidates()
        return ans
