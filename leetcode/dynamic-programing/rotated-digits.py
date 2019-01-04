# https://leetcode.com/problems/rotated-digits/
# http://www.cnblogs.com/grandyang/p/9154892.html

class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        # dp[i]: 0, invalid; 1, rotate to themselves; 2, good
        dp = [0] * (N + 1)
        res = 0
        for i in xrange(N + 1):
            if i < 10:
                if i in {2, 5, 6, 9}:
                    dp[i] = 2
                    res += 1
                elif i in {0, 1, 8}:
                    dp[i] = 1
            else:
                a, b = dp[i / 10], dp[i % 10]
                if a == 2 and b > 0 or a > 0 and b == 2:
                    dp[i] = 2
                    res += 1
                elif a == 1 and b == 1:
                    dp[i] = 1
        return res
