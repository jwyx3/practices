# https://leetcode.com/problems/candy-crush/
# https://leetcode.com/problems/candy-crush/solution/
# Time: O((3*R*C) * (R*C/3)), each recursion may elimiate 3, so we may need to (R*C/3) call stacks
# Space: O(1)

class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        R, C = len(board), len(board[0])
        todo = False
        
        # crush
        for r in xrange(R):
            for c in xrange(C-2):
                if abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) != 0:
                    board[r][c] = board[r][c+1] = board[r][c+2] = -abs(board[r][c])
                    todo = True
        for c in xrange(C):
            for r in xrange(R-2):
                if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
                    board[r][c] = board[r+1][c] = board[r+2][c] = -abs(board[r][c])
                    todo = True
        # gravity
        for c in xrange(C):
            wr = R - 1
            for r in xrange(R-1, -1, -1):
                if board[r][c] > 0:
                    board[wr][c] = board[r][c]
                    wr -= 1
            for r in xrange(wr, -1, -1):
                board[r][c] = 0
        
        return self.candyCrush(board) if todo else board
