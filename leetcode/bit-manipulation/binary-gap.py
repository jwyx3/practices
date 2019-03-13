# https://leetcode.com/problems/binary-gap/
# https://leetcode.com/problems/binary-gap/solution/
# Time: O(logN)
# Space: O(1)

class Solution(object):
    def binaryGap(self, n):
        """
        :type N: int
        :rtype: int
        """
        ans, last = 0, None
        for i in xrange(32):
            if n & 1:
                if last is not None:
                    ans = max(ans, i - last)
                last = i
            n >>= 1
        return ans
