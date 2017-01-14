class Solution:
    # @param {list[list[str]]} board a 2D board containing 'X' and 'O'
    # @return nothing

    # BFS, start from boundaries to find all unsurrounded regions
    def surroundedRegions(self, board):
        def fill(board, i, j):
            n, m = len(board), len(board[0])
            delta = [(0, -1), (0, 1), (1, 0), (-1, 0)]
            if i >= 0 and i < n and j >= 0 and j < m and board[i][j] == 'O':
                board[i][j] = 'D'
                for di, dj in delta:
                    ni, nj = i + di, j + dj
                    fill(board, ni, nj)

        if not board or not board[0]:
            return
        n, m = len(board), len(board[0])
        for i in xrange(n):
            fill(board, i, 0)
            fill(board, i, m - 1)
        for j in xrange(m):
            fill(board, 0, j)
            fill(board, n - 1, j)

        for i in xrange(n):
            for j in xrange(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'D':
                    board[i][j] = 'O'

