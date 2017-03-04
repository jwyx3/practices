class Solution:
    """
    Calculate the total number of distinct N-Queen solutions.
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def totalNQueens(self, n):
        if n <= 0:
            return 0
        self.result = 0
        board = [0] * n
        self.dfs(board, 0)
        return self.result

    def dfs(self, board, x):
        n = len(board)
        if x == n:
            self.result += 1
            return
        for y in range(n):
            if self.noAttack(board, x, y):
                board[x] |= (1 << y)
                self.dfs(board, x + 1)
                board[x] = 0

    # board doesn't include x, y
    def noAttack(self, board, x, y):
        n = len(board)
        # row
        if board[x]:
            return False
        # column
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

