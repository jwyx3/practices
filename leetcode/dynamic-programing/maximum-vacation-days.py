# https://leetcode.com/problems/maximum-vacation-days
# Time: O(N**2 * K)
# Space: O(N)

class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        # dp(i, j): max vacation days from city j at week i
        # dp(i, j) = max(days[k][i] + dp(i+1, k)), k=0..n-1
        # initial: dp(i,m) = 0
        # answer: dp(0, 0)
        n, m = len(flights), len(days[0])
        dp = [[0] * n for _ in xrange(2)]
        for i in xrange(m-1, -1, -1):
            for j in xrange(n):
                dp[i%2][j] = max(
                    (days[k][i] + dp[(i+1)%2][k])
                    for k in xrange(n) if flights[j][k] or j == k) 
        return dp[0][0]

