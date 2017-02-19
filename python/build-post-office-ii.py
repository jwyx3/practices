import Queue
import sys
from collections import deque

# BFS from house, use two array
class Solution2:
    def shortestDistance(self, grid):
        # steps:
        # 1) run BFS on all houses
        # 2) record distance sum to all houses at each empty cell (initial maxint)
        # 3) record number of houses can be reachable at each empty cell (initial 0)
        # 4) get min sum of distances at each empty cell
        if not grid or not grid[0]:
            return -1
        m, n = len(grid), len(grid[0])
        dist = [[sys.maxint for j in xrange(n)] for i in xrange(m)]
        reachable = [[0 for j in xrange(n)] for i in xrange(m)]
        total_houses = 0

        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    total_houses += 1
                    self.bfs(i, j, grid, m, n, dist, reachable)

        ans = sys.maxint
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 0 and dist[i][j] < ans and\
                        reachable[i][j] == total_houses:
                    ans = dist[i][j]
        if ans == sys.maxint:
            return -1
        return ans

    def bfs(self, i, j, grid, m, n, dist, reachable):
        q = deque([(i, j, 0)])
        d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        # the i, j will overwrite parameters
        visited = [[0 for j in xrange(n)] for i in xrange(m)]
        while len(q) > 0:
            x, y, l = q.popleft()
            if dist[x][y] == sys.maxint:
                dist[x][y] = 0
            dist[x][y] += l
            reachable[x][y] += 1
            for dx, dy in d:
                nx, ny = dx + x, dy + y
                if nx >= 0 and nx < m and ny >= 0 and ny < n\
                        and grid[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny, l + 1))


# BFS from house, but still TLE!!
class Solution1:
    # @param {int[][]} grid a 2D grid
    # @return {int} an integer
    def shortestDistance(self, grid):
        # steps
        # 1) run BFS for all houses
        # 2) get list of empty cells for all houses
        # 3) return shortest distance
        if not grid or not grid[0]:
            return -1
        n, m = len(grid), len(grid[0])
        distances = {}
        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == 0:
                    distances[(i, j)] = []
        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == 1:
                    self._shortestDistance(grid, i, j, distances)
        ans = sys.maxint
        for _, v in distances.items():
            if sys.maxint in v:
                continue
            ans = min(ans, sum(v))
        if ans == sys.maxint:
            return -1
        return ans

    def _shortestDistance(self, grid, x, y, distances):
        n, m = len(grid), len(grid[0])
        record = [[sys.maxint for _ in xrange(m)] for i in xrange(n)]
        q = Queue.Queue(maxsize=n * m)
        q.put((x, y))
        record[x][y] = 0
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while not q.empty():
            curt_x, curt_y = q.get()
            for dx, dy in d:
                nx, ny = curt_x + dx, curt_y + dy
                if nx >= 0 and nx < n and ny >= 0 and ny < m and\
                        record[curt_x][curt_y] + 1 < record[nx][ny]:
                    record[nx][ny] = record[curt_x][curt_y] + 1
                    # can only pass through empty
                    if grid[nx][ny] == 0:
                        q.put((nx, ny))

        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == 0:
                    distances[(i, j)].append(record[i][j])

class Solution:
    # @param {int[][]} grid a 2D grid
    # @return {int} an integer
    def shortestDistance(self, grid):
        # steps
        # 1) run BFS for all empty cell
        # 2) get sum of all houses and check imposibility (one of sum is maxint)
        # 3) return shortest distance (-1 if result is maxint)
        if not grid or not grid[0]:
            return -1
        n, m = len(grid), len(grid[0])
        ans = sys.maxint
        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == 0:
                    ans = min(ans, self._shortestDistance(grid, i, j))
        if ans == sys.maxint:
            return -1
        return ans

    # BFS from empty
    # TLE!!
    def _shortestDistance(self, grid, x, y):
        n, m = len(grid), len(grid[0])
        record = [[sys.maxint for _ in xrange(m)] for i in xrange(n)]
        q = Queue.Queue(maxsize=n * m)
        q.put((x, y))
        record[x][y] = 0
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while not q.empty():
            curt_x, curt_y = q.get()
            for dx, dy in d:
                nx, ny = curt_x + dx, curt_y + dy
                if nx >= 0 and nx < n and ny >= 0 and ny < m and\
                        record[curt_x][curt_y] + 1 < record[nx][ny]:
                    record[nx][ny] = record[curt_x][curt_y] + 1
                    # can only pass through empty
                    if grid[nx][ny] == 0:
                        q.put((nx, ny))

        ans = 0
        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == 1:
                    if record[i][j] == sys.maxint:
                        return sys.maxint
                    ans += record[i][j]
        return ans


if __name__ == '__main__':
    s = Solution2()
    print s.shortestDistance([[0,1,0,0,0],[1,0,0,2,1],[0,1,0,0,0]])
