# https://leetcode.com/problems/convert-to-base-2/
# the last bit determine whether the last bit is odd/even
# Time: O(logN)
# Space: O(logN)

class Solution(object):
    def baseNeg2(self, n):
        """
        :type N: int
        :rtype: str
        """
        if n == 0:
            return '0'
        # only last bit will impact odd/even
        ans, k = [], 0
        while n:
            if n & 1:  # odd
                ans.append(1)
                n -= (1 - (k & 1)) - (k & 1)
            else:
                ans.append(0)
            k += 1
            n >>= 1
        return ''.join(map(str, ans[::-1]))

# https://leetcode.com/problems/convert-to-base-2/discuss/265507/JavaC%2B%2BPython-2-lines-Exactly-Same-as-Base-2
# simpler idea: x = -(x >> 1)
# for 2，x = x >> 1. e.g. x = (2) ^ 2 + (2) ^ 1 + (2) ^ 0 = 3
# (2) ^ 2 + (2) ^ 1 + (2) ^ 0 -> (2) ^ 1 + (2) ^ 0 -> (2) ^ 0 -> 0
# for -2, x = -(x >> 1). e.g. x = (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3
# (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 -> -((-2) ^ 1 + (-2) ^ 0) -> (-2) ^ 0 -> 0

class Solution(object):
    def baseNeg2(self, n):
        """
        :type N: int
        :rtype: str
        """
        if n == 0:
            return '0'
        ans = []
        while n:
            ans.append(n & 1)
            n = -(n >> 1)
        return ''.join(map(str, ans[::-1]))
