class Solution:
    # @param: a matrix of integers
    # @return: a list of integers
    def printZMatrix(self, matrix):
        if not matrix or not matrix[0]:
            return []
        n, m = len(matrix), len(matrix[0])
        delta = [(-1, 1), (1, -1)]
        direction = 0
        result, x, y = [], 0, 0
        for i in range(n * m):
            result.append(matrix[x][y])
            dx, dy = delta[direction]
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                if direction == 0:
                    if ny >= m:
                        nx, ny = x + 1, y
                    else:
                        nx, ny = x, y + 1
                else:
                    if nx >= n:
                        nx, ny = x, y + 1
                    else:
                        nx, ny = x + 1, y
                direction = 1 - direction
            x, y = nx, ny
        return result

