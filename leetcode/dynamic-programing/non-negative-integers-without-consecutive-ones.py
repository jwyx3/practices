# https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/
# https://blog.csdn.net/magicbean2/article/details/78968556
# Time: O(logN)
# Space: O(logN)
# same prefix or different ranges

class Solution(object):
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        dp = [0] * 32
        # 00000-11111 -> 00000-01111, 10000-10111, 11000-11111 (invalid)
        # f(5) = f(4) + f(3)
        dp[0], dp[1] = 1, 2
        for i in xrange(2, len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
        prev_bit = ans = 0
        # 1 <= n <= 10**9 < 2**30, so 0<=i<=30
        # think as different ranges
        # 10010
        #   00000-01111
        #   10000-10001
        #   10010-10010
        for i in xrange(30, -1, -1):
            # flip 1 << i, there are i bits.
            if num & (1 << i):
                ans += dp[i]
                if prev_bit:  # if 11, stop
                    return ans
                prev_bit = 1
            else:
                prev_bit = 0
        return ans + 1
