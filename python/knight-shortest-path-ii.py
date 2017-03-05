from collections import deque


class Solution:
    # @param {boolean[][]} grid a chessboard included 0 and 1
    # @return {int} the shortest path

    # BFS: shortest graph
    def shortestPath2(self, grid):
        if not grid or not grid[0] or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        n, m = len(grid), len(grid[0])
        delta = [(1, 2), (-1, 2), (2, 1), (-2, 1)]
        q = deque([(0, 0, 0)])
        while q:
            x, y, distance = q.popleft()
            if x == n - 1 and y == m - 1:
                return distance
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < n and ny >= 0 and ny < m and\
                        grid[nx][ny] == 0:
                    q.append((nx, ny, distance + 1))
                    grid[nx][ny] = 2
        return -1
