class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        if n <= 0:
            return []
        board, result = [0] * n, []
        self.dfs(board, 0, result)
        for i in range(len(result)):
            result[i] = self.convertBoard(result[i])
        return result

    def convertBoard(self, board):
        n = len(board)
        for i in range(n):
            num, board[i] = board[i], ''
            for j in range(n):
                if num & 1:
                    board[i] += 'Q'
                else:
                    board[i] += '.'
                num >>= 1
        return board

    def dfs(self, board, x, result):
        n = len(board)
        if x == n:
            result.append(board[:])
            return
        for y in range(n):
            if self.noAttack(board, x, y):
                board[x] |= (1 << y)
                self.dfs(board, x + 1, result)
                board[x] = 0

    # board doesn't have x, y
    def noAttack(self, board, x, y):
        n = len(board)
        if board[x]:
            return False
        for i in range(n):
            if board[i] & (1 << y):
                return False
        delta = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
        for dx, dy in delta:
            nx, ny = x, y
            while nx >= 0 and nx < n and ny >= 0 and ny < n:
                if board[nx] & (1 << ny):
                    return False
                nx, ny = nx + dx, ny + dy
        return True

