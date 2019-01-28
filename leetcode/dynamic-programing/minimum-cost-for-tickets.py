# https://leetcode.com/problems/minimum-cost-for-tickets/
# https://leetcode.com/problems/minimum-cost-for-tickets/solution/
# https://www.acwing.com/solution/LeetCode/content/877/
# Time: O(N)
# Space: O(N)

class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        # dp[i]: min cost for first i days
        # dp[i] = min(dp[j] + cost[k])
        # initial: dp[0] = 0, dp[i>0] = float('inf')
        # answer: dp[len(days)]
        
        N = len(days)
        dp = [float('inf')] * (N + 1)
        dp[0] = 0
        
        days = [0] + days
        for i in xrange(1, N + 1):
            for j in xrange(i, 0, -1):
                if days[i] - days[j] < 1:
                    # buy ticket at days[j], the cost is dp[j-1] + costs[0]
                    dp[i] = min(dp[i], dp[j-1] + costs[0])
                if days[i] - days[j] < 7:
                    dp[i] = min(dp[i], dp[j-1] + costs[1])
                if days[i] - days[j] < 30:
                    dp[i] = min(dp[i], dp[j-1] + costs[2])
                else:
                    break
        return dp[N]
