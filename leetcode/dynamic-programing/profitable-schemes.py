# https://leetcode.com/problems/profitable-schemes/
# https://leetcode.com/problems/profitable-schemes/discuss/154617/C%2B%2BJavaPython-DP
# Knapsack
# Time: (N*P*G)
# Space; O(P*G)

class Solution(object):
    def profitableSchemes(self, G, P, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        # dp[k][i][j]: the number of schemes with profitability i and requiring j gang members
        # dp[k][min(P, i+profit[k])][j+group[k]] += dp[k-1][i][j]
        # initial: dp[k][0][0] = 1, otherwise, 0
        # answer: sum(dp[N][P])
        # -> reduce 1d
        # dp[i][j] and update in reversed way
        MOD = 10 ** 9 + 7
        n = len(group)
        dp = [[0] * (G + 1) for _ in xrange(P + 1)]
        dp[0][0] = 1
        
        for k in xrange(n):
            p, g = profit[k], group[k]
            # update in reversed way to avoid 
            for i in xrange(P, -1, -1):
                p2 = min(P, i + p)
                for j in xrange(G - g, -1, -1):
                    g2 = j + g 
                    dp[p2][g2] += dp[i][j]
                    dp[p2][g2] %= MOD
        return sum(dp[P]) % MOD
