# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __str__(self):
        return "[%d, %d]" % (self.x, self.y)

import Queue
import sys

class Solution:
    def shortestPath(self, grid, source, destination):
        src, dst = source, destination
        if src is None or dst is None or\
                grid[src.x][src.y] or grid[dst.x][dst.y]:
            return -1
        n, m = len(grid), len(grid[0])
        d = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
        records = [[sys.maxint for _ in range(m)] for i in range(n)]

        q = Queue.Queue(maxsize= n * m)
        q.put(src)
        records[src.x][src.y] = 0

        while not q.empty():
            curt = q.get()
            if curt.x == dst.x and curt.y == dst.y:
                return records[curt.x][curt.y]
            for dx, dy in d:
                nx, ny = curt.x + dx, curt.y + dy
                if nx >= 0 and nx < n and ny >= 0 and ny < m and not grid[nx][ny] and\
                        records[curt.x][curt.y] + 1 < records[nx][ny]:
                    records[nx][ny] = records[curt.x][curt.y] + 1
                    q.put(Point(nx, ny))
        return -1

    # @param {boolean[][]} grid a chessboard included 0 (False) and 1 (True)
    # @param {Point} source a point
    # @param {Point} destination a point
    # @return {int} the shortest path
    # TLE!!
    def shortestPath1(self, grid, source, destination):
        src, dst = source, destination
        if src is None or dst is None or\
                grid[src.x][src.y] or grid[dst.x][dst.y]:
            return -1
        d = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
        n, m = len(grid[0]), len(grid)
        visited = [[0 for _ in range(n)] for i in range(m)]

        q = Queue.Queue(maxsize = n * m)
        q.put(src)
        ans = 0

        while not q.empty():
            size = q.qsize()
            for _ in range(size):
                curt = q.get()
                # found ans
                if curt.x == dst.x and curt.y == dst.y:
                    return ans
                # handle next
                visited[curt.x][curt.y] = 1
                for dx, dy in d:
                    nx, ny = curt.x + dx, curt.y + dy
                    if self.inBound(nx, ny, grid) and not visited[nx][ny]:
                        q.put(Point(nx, ny))
            ans += 1
        # not found
        return -1

    def inBound(self, x, y, grid):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
        if grid[x][y]:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    print s.shortestPath([[0,1,0],[0,0,1],[0,0,0]], Point(2, 0), Point(2, 2))
    print s.shortestPath([[0,0,0],[0,0,0],[0,0,0]], Point(2, 0), Point(2, 2))
    print s.shortestPath([[0,1,0],[0,0,0],[0,0,0]], Point(2, 0), Point(2, 2))
