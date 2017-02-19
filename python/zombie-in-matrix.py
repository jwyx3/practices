import Queue


class Solution:
    # @param {int[][]} grid  a 2D integer grid
    # @return {int} an integer
    def zombie(self, grid):
        # need level info
        if not grid or not grid[0]:
            return -1
        n, m = len(grid), len(grid[0])
        q = Queue.Queue(maxsize=n * m)
        people_count = 0
        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == 0:
                    people_count += 1
                elif grid[i][j] == 1:
                    q.put((i, j))

        days = 0
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while not q.empty():
            size = q.qsize()
            days += 1
            for _ in xrange(size):
                curt = q.get()
                for dx, dy in d:
                    nx, ny = curt[0] + dx, curt[1] + dy
                    if nx >= 0 and nx < n and ny >= 0 and ny < m and\
                            grid[nx][ny] == 0:
                        people_count -= 1
                        if people_count == 0:
                            return days
                        grid[nx][ny] = 1
                        q.put((nx, ny))
        return -1
