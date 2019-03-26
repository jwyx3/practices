# https://leetcode.com/problems/largest-palindrome-product/
# http://www.cnblogs.com/grandyang/p/7644725.html
# Time: O(10**(2N)) ??
# Space: O(1)

class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n > 1:
            lo, hi = 10**(n - 1) - 1, 10**n - 1
            for b in xrange(hi, lo, -1):
                # construct palindrome
                p = int(str(b) + str(b)[::-1])
                x = hi
                # if x*y == p, only consider max(x, y)
                while x * x >= p:
                    if p % x == 0:
                        return p % 1337
                    x -= 1
        return 9
