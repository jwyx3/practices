# https://leetcode.com/problems/soup-servings/
# https://leetcode.com/problems/soup-servings/solution/
# https://leetcode.com/problems/soup-servings/discuss/121711/C%2B%2BJavaPython-When-N-greater-4800-just-return-1
# Time: O(N**2) or O(1)
# Space: O(N**2) or O(1)

class Solution(object):
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        # dp[i][j]: probability of i ml A and j ml B
        # f(x) = max(0, x)
        # dp[i][j] = 0.25 * (
        #   dp[f(i-100)][j] +
        #   dp[f(i-75)][f(j-25)] +
        # . dp[f(i-50)][f(j-50)] +
        #   dp[f(i-25)][f(j-75)])
        # initial: dp[0][0] = 0.5, dp[>0][0] = 1, dp[0][>0] = 0
        # answer: dp[N][N]
        # 1 serving = 25 ml
        M = lambda x: max(x, 0)
        quot, rem = divmod(N, 25)
        N = quot + (rem > 0)
        if N >= 200:
            return 1.0
        dp = [[0] * (N + 1) for _ in xrange(N + 1)]
        dp[0][0] = 0.5
        for j in xrange(1, N + 1):
            dp[0][j] = 1
        for i in xrange(1, N + 1):
            for j in xrange(1, N + 1):
                dp[i][j] = 0.25 * (
                    dp[M(i-4)][j] + dp[M(i-3)][M(j-1)] + dp[M(i-2)][M(j-2)] + dp[M(i-1)][M(j-3)])
        return dp[N][N]
