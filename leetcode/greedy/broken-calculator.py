# https://leetcode.com/problems/broken-calculator/
# Time: O(logY)
# Space: O(1)

class Solution(object):
    def brokenCalc(self, x, y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        # multiple first until x >= y
        ans = 0
        while x < y:
            x <<= 1
            ans += 1
        # the diff d can be a0 + a1*2 + a2*4 + ... + ak * (1<<k)
        # ak should be as large as possible
        d, k = x - y, ans
        while d:
            base = 1 << k
            if d >= base:
                quot, rem = divmod(d, base)
                ans += quot
                d = rem
            k -= 1
        return ans
