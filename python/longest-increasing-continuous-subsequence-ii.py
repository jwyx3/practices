class Solution:
    # @param {int[][]} A an integer matrix
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequenceII(self, A):
        if not A or len(A[0]) == 0:
            return 0
        ans, n, m = 1, len(A), len(A[0])
        self.delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.dp = [[0 for y in xrange(m)] for x in xrange(n)]
        for x in xrange(n):
            for y in xrange(m):
                self.search(A, x, y)
                ans = max(ans, self.dp[x][y])
        return ans

    def search(self, A, x, y):
        if self.dp[x][y] != 0:
            return self.dp[x][y]
        # don't need visited because it's increasing
        ans, n, m = 1, len(A), len(A[0])
        for dx, dy in self.delta:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < n and ny >= 0 and ny < m and A[nx][ny] < A[x][y]:
                ans = max(ans, self.search(A, nx, ny) + 1)
        # memorize
        self.dp[x][y] = ans
        return self.dp[x][y]

if __name__ == '__main__':
    s = Solution()
    print s.longestIncreasingContinuousSubsequenceII([
      [1 ,2 ,3 ,4 ,5],
      [16,17,24,23,6],
      [15,18,25,22,7],
      [14,19,20,21,8],
      [13,12,11,10,9]
    ]), '#', '25'
