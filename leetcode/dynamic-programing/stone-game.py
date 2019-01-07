# https://leetcode.com/problems/stone-game/
# Time: O(N*N)
# Space: O(N*N)

class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        # dp[i][j]: the number of most stones current user can get for piles[i:j+1]
        # dp[i][j] = sum(piles[i:j+1]) - min(dp[i+1][j], dp[i][j-1]), i <= j
        # initial: dp[i][i] = piles[i]
        # answer: dp[0][N-1] > sum(piles) / 2
        N = len(piles)
        dp = [[0] * N for _ in xrange(N)]
        for i in xrange(N):
            dp[i][i] = piles[i]
        for i in xrange(N - 2, -1, -1):
            s = piles[i]
            for j in xrange(i + 1, N):
                s += piles[j]
                dp[i][j] = s - min(dp[i+1][j], dp[i][j-1])
        return dp[0][N-1] > sum(piles) / 2

# TODO: Time O(1)
# Alex always win!
# https://leetcode.com/problems/stone-game/solution/
