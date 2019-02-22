# https://leetcode.com/problems/cherry-pickup/
# https://leetcode.com/problems/cherry-pickup/solution/
# convert problem into two persons pick cherries from (0,0) at the same time
# Time: O(N**3)
# Space: O(N**2)
# t = row + col.

class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # dp[t][i][j]: the most cherries two persons can pick from
        #           (0,0) to (i, t-i), (j, t-j)
        # dp[t][i][j] = max(dp[t-1][ni][nj] for ni, nj in [(i-1, j-1), (i, j-1), (i-1, j), (i, j)])
        #               + grid[i][t-i] + (grid[j][t-j] if i != j else 0)
        #               if grid[i][t-i] >= 0 and grid[j][t-j] >= 0
        # initial: dp[0][0][0] = grid[0][0]
        # answer: dp[2*N-2][N-1][N-1]
        
        if not grid or not grid[0]:
            return 0
        N = len(grid)
        dp = [[float('-inf')] * N for _ in xrange(N)]
        dp[0][0] = grid[0][0]
        for t in xrange(1, 2 * N - 1):
            dp2 = [[float('-inf')] * N for _ in xrange(N)]
            # t = 0..2*N-2, i = 0..N-1, so 
            for i in xrange(max(0, t-(N-1)), min(N-1, t) + 1):
                for j in xrange(max(0, t-(N-1)), min(N-1, t) + 1):
                    if grid[i][t-i] < 0 or grid[j][t-j] < 0:
                        continue
                    delta = grid[i][t-i]
                    if i != j:
                        delta += grid[j][t-j]
                    dp2[i][j] = max(
                        dp[ni][nj] + delta
                        for ni in (i-1, i)
                        for nj in (j-1, j)
                        if ni >= 0 and nj >= 0)
            dp = dp2
        return max(0, dp[N-1][N-1])
