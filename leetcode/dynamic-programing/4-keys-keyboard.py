# https://leetcode.com/problems/4-keys-keyboard/
# Time: O(n*n)
# Space: O(n)

class Solution(object):
    def maxA(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[i]: max numbers of 'A' for i presses
        # dp[i] = max{dp[j] * (i - j - 1)}. 1<=j<=i-3
        # i-3 => at least 3 more steps, we can use copy
        # i - j - 1 => i - j - 2 extra copies + 1 original copy
        # Initial: dp[i] = i, don't copy
        # Answer: dp[n]
        dp = range(n + 1)
        for i in xrange(4, n + 1):
            for j in xrange(1, i - 3 + 1):
                dp[i] = max(dp[i], dp[j] * (i - j - 1))
        return dp[n]
        
