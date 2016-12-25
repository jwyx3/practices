import heapq

class Cell(object):
    def __init__(self, x, y, h):
        self.x = x
        self.y = y
        self.height = h

class Solution:
    # @param heights: a matrix of integers
    # @return: an integer
    def trapRainWater(self, heights):
        # write your code here
        row = len(heights)
        if row <= 1:
            return 0
        col = len(heights[0])
        if col <= 1:
            return 0

        # handle boundaries
        # the cell at the boundary can not hold any water
        heap = []
        visited = [[False for _ in xrange(col)] for _ in xrange(row)]
        for y in xrange(col):
            for x in [0, row - 1]:
                if not visited[x][y]:
                    visited[x][y], h = True, heights[x][y]
                    heapq.heappush(heap, (h, Cell(x, y, h)))
        for x in xrange(row):
            for y in [0, col - 1]:
                if not visited[x][y]:
                    visited[x][y], h = True, heights[x][y]
                    heapq.heappush(heap, (h, Cell(x, y, h)))

        ans = 0
        while True:
            try:
                # min heap, new_height is the sum of cell height and water height
                # the key of heap is new_height
                new_height, cell = heapq.heappop(heap)
                # get the water height
                ans += (new_height - cell.height)
                for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    nx, ny = cell.x + dx, cell.y + dy
                    if nx >= 0 and nx < row and ny >= 0 and ny < col and not visited[nx][ny]:
                        # nh is the new_height of new cell
                        visited[nx][ny], nh = True, max(heights[nx][ny], new_height)
                        heapq.heappush(heap, (nh, Cell(nx, ny, heights[nx][ny])))
            except IndexError:
                # if empty
                break
        return ans
