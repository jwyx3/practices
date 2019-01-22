# https://leetcode.com/problems/flip-string-to-monotone-increasing/
# https://leetcode.com/problems/flip-string-to-monotone-increasing/solution/
# Time: O(N)
# Space: O(1)

class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        # dp0[i]: min flips to make S monotone increasing and ending with 0 (first i elements)
        # dp1[i]: min flips to make S monotone increasing and ending with 1 (first i elements)
        # bit = int(S[i-1])
        # dp0[i] = dp0[i-1] + (bit ^ 0)
        # dp1[i] = min(dp0[i-1], dp1[i-1]) + (bit ^ 1)
        # initial: dp0[0] = dp1[0] = 0
        # answer: min(dp0[len(S)], dp1[len(S)])
        # note: the precedence of ^ is lower than +
        N = len(S)
        dp0 = dp1 = 0
        for i in xrange(1, N + 1):
            bit = int(S[i-1])
            dp1 = min(dp0, dp1) + (bit ^ 1)
            dp0 = dp0 + (bit ^ 0)
        return min(dp0, dp1)
