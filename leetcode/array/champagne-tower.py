# https://leetcode.com/problems/champagne-tower/
# https://leetcode.com/problems/champagne-tower/solution/
# simulation
# Time: O(R**2)
# Space: O(R**2)

class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        # dp[r][c]: the total poured champagne for this cup
        R = query_row + 1
        dp = [[0] * R for _ in xrange(2)]
        dp[0][0] = poured
        for r in xrange(1, R):
            for c in xrange(r + 1):
                p = max(0, dp[(r-1)%2][c] - 1)
                if c > 0:
                    p += max(0, dp[(r-1)%2][c-1] - 1)
                dp[r%2][c] = p / 2.0
        return min(1, dp[query_row%2][query_glass])
