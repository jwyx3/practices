# https://leetcode.com/problems/minesweeper/
# or use BFS
# Time: O(M*N)
# Space: O(1) 

class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if not board or not board[0]:
            return board
        
        m, n = len(board), len(board[0])
        # return (unreveal squares, current revealed square)
        def neighbors(x, y):
            mines, squares = 0, []
            # adjacent mines are 8 directions
            for nx, ny in [
                    (x+1, y), (x-1, y), (x, y+1), (x, y-1),
                    (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)]:
                if 0 <= nx < m and 0 <= ny < n:
                    if board[nx][ny] in ('M', 'E'):
                        squares.append((nx, ny))
                    if board[nx][ny] == 'M':
                        mines += 1
            return squares, str(mines) if mines > 0 else 'B'
        
        def dfs(x, y):
            nodes, board[x][y] = neighbors(x, y)
            if board[x][y] != 'B':
                return
            for nx, ny in nodes:
                dfs(nx, ny)
                    
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
        elif board[x][y] == 'E':
            dfs(x, y)
        return board
