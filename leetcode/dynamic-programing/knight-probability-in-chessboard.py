# https://leetcode.com/problems/knight-probability-in-chessboard/
# Time: O(R*C)
# Space: O(R*C)

class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        # dp[x][y][k]: probability that knight locate at x,y after k moves
        # dp[x][y][k] = sum(dp[nx][ny][k-1]) * 0.125
        # initial: dp[r][c][0] = 1, otherwise 0
        # answer: sum(dp[*][*])
        
        delta = [(-2, 1), (-1, 2), (1, 2), (2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        dp = [[[0] * 2 for x in xrange(N)] for y in xrange(N)]
        dp[r][c][0] = 1
        
        def neighbors(x, y):
            for dx, dy in delta:
                nx, ny = dx + x, dy + y
                if 0 <= nx < N and 0 <= ny < N:
                    yield nx, ny
        
        for k in xrange(1, K + 1):
            for x in xrange(N):
                for y in xrange(N):
                    dp[x][y][k%2] = 0
            for x in xrange(N):
                for y in xrange(N):
                    for nx, ny in neighbors(x, y):
                        dp[nx][ny][k%2] += 0.125 * dp[x][y][(k-1)%2]
        return sum(dp[x][y][K%2] for x in xrange(N) for y in xrange(N))
