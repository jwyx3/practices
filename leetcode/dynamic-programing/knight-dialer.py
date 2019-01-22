# https://leetcode.com/problems/knight-dialer/
# Time: O(N)
# Space: O(1)

class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        # dp[i][j]: how many distinct numbers can you dial for i hops and ending with digit j
        # dp[i][j] = sum{dp[i-1][k]}, all k can knight jump to j
        # initial: dp[0][*] = 1
        # answer: sum(dp[N-1])
        # special case: dp[0][5] = 1, dp[>0][5] = 0
        MOD = 10 ** 9 + 7
        dp = [[1] * 10 for _ in xrange(2)]
        neighbors = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        for i in xrange(1, N):
            for j in xrange(10):
                dp[i%2][j] = sum(dp[(i-1)%2][nei] % MOD for nei in neighbors[j])
        return sum(dp[(N-1)%2]) % MOD
