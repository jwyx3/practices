# https://leetcode.com/problems/smallest-good-base/
# n = a0 + a1*k + a2*k**2 + ... + ax*k**x, a0 = a1 = a2 = ... = ax = 1
# n = 1 + k + k**2 + ... + k**x = (a0 - ax*k) / (1 - k) = (k**(x+1) - 1) / (k - 1) = f(k)
# when k >= 2 and given x, f(k) is monotonic. k inc, f(k) inc

class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        # max length of 1111 is m = len(bin(n)) - 2
        # n = a0 + a1*k + a2*k**2 + ... + ax*k**x
        # max x can be m - 1
        n = int(n)
        m = len(bin(n)) - 2
        # x desc, k asc. so x from m - 1 to 1
        for x in xrange(m, 0, -1):
            lo, hi = 2, n - 1
            while lo < hi:
                k = (lo + hi) / 2
                # f = (k**(x+1) - 1) / (k - 1)
                # f == n
                # n*(k-1) == k**(x+1) - 1
                num, deno = k**(x+1) - 1, n*(k-1)
                if num == deno:
                    return str(k)
                elif num > deno:
                    hi = k
                else:
                    lo = k + 1
        return str(n - 1)
