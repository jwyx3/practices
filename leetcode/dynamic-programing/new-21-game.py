# https://leetcode.com/problems/new-21-game/
# https://leetcode.com/problems/new-21-game/solution/
# Time: O(K + W)
# Space: O(W) 

class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        # dp[x]: the probability when Alice has x stone
        # dp[x] = 1.0/W*sum(dp[x+1:x+W+1])
        # initial: dp[K..min(N, W)] = 1.0, dp[min(N, W)+1..W] = 0.0
        # answer: dp[0]
        # use S to reduce time O(1)
        # dp[x] = 1/W*(dp[x+1]+ ... + dp[x+W])
        # dp[x-1] = 1/W*(dp[x]+ ... + dp[x+W-1])
        # assume S = dp[x+1]+ ... + dp[x+W]
        # then dp[x] = 1/W*S
        # S1 = S + dp[x] - dp[x+W]
        # dp[x-1] = 1/W*S1
        
        mod = W + 1  # use W+1 to avoid dp[(x+W)%mod] by dp[x%mod] 
        dp = [0] * mod
        # if K <= x <= N, p = 1.0
        for x in xrange(K, min(N + 1, K + W)):
            dp[x%mod] = 1.0
        s = min(N - K + 1, W)
        for x in xrange(K-1, -1, -1):
            dp[x%mod] = s / float(W)
            s += dp[x%mod] - dp[(x+W)%mod]
        return dp[0]
