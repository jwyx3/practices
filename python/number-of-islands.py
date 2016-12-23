from collections import namedtuple

class Solution:
    Island = namedtuple('Island', ['x', 'y'])
    count = 0
    father = None

    def find(self, island):
        x, y = island.x, island.y
        if (self.father[x][y] == None):
            return island
        self.father[x][y] = self.find(self.father[x][y])
        return self.father[x][y]

    def union(self, island1, island2):
        r1 = self.find(island1)
        r2 = self.find(island2)
        if r1 != r2:
            self.father[r1.x][r1.y] = r2
            self.count -= 1

    def query(self):
        return self.count

    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        # corner case:
        # 1. grid is empty
        if grid:
            self.count = 0
            row_len, col_len = len(grid), len(grid[0])
            self.father = [[None for col in xrange(col_len)] for row in xrange(row_len)]

            for row in xrange(row_len):
                for col in xrange(col_len):
                    if grid[row][col]:
                        self.count += 1
                        if col - 1 >= 0 and grid[row][col - 1]:
                            self.union(self.Island(row, col - 1), self.Island(row, col))
                        if row - 1 >= 0 and grid[row - 1][col]:
                            self.union(self.Island(row - 1, col), self.Island(row, col))
                        if col + 1 < col_len and grid[row][col + 1]:
                            self.union(self.Island(row, col + 1), self.Island(row, col))
                        if row + 1 < row_len and grid[row + 1][col]:
                            self.union(self.Island(row + 1, col), self.Island(row, col))
        return self.query()
