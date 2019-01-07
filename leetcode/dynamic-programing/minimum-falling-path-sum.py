# https://leetcode.com/problems/minimum-falling-path-sum/
# Time: O(N**2)
# Space: O(N)

class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        # dp[i][j]: min{dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]} + A[i][j]
        # inital: dp[0][j] = A[0][j]
        # answer: min(dp[r-1])
        R, C = len(A), len(A[0])
        dp = [[0] * C for _ in xrange(2)]
        for c in xrange(C):
            dp[0][c] = A[0][c]
        for r in xrange(1, R):
            for c in xrange(C):
                dp[r%2][c] = dp[(r-1)%2][c]
                if c - 1 >= 0:
                    dp[r%2][c] = min(dp[r%2][c], dp[(r-1)%2][c-1])
                if c + 1 < C:
                    dp[r%2][c] = min(dp[r%2][c], dp[(r-1)%2][c+1])
                dp[r%2][c] += A[r][c]
        return min(dp[(R-1)%2])

# https://leetcode.com/problems/minimum-falling-path-sum/solution/
# use A as dp, and process from N to 0
# Time: O(N**2)
# Space: O(1)

class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        while len(A) >= 2:
            row = A.pop()
            for i in xrange(len(row)):
                A[-1][i] += min(row[max(0, i - 1):min(len(row), i + 2)])
        return min(A[0])
