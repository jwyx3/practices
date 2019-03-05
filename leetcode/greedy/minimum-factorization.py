# https://leetcode.com/problems/minimum-factorization/
# Time: O(logN)
# Space: O(logN)

class Solution(object):
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        # quot, rem = divmod(a, k), k=9..2
        # f(48), 9 = 5, 4
        # f(48), 8 = 6, 0 -> 10 * f(6) + 8
        # f(6), 9 = 0, 6
        # ...
        # f(6), 6 = 1, 0 -> 10 * f(1) + 6
        # ...
        # f(1) = 0
        if a == 1:
            return 1
        MAX_INT = (1<<31) - 1
        def f(x):
            if x == 1:
                return True, 0
            for d in xrange(9, 1, -1):
                quot, rem = divmod(x, d)
                if rem == 0:
                    valid, ans = f(quot)
                    if not valid:
                        return False, 0
                    ans = 10 * ans + d
                    if ans > MAX_INT:
                        return False, 0
                    return True, ans
            return False, 0
        valid, ans = f(a)
        return ans if valid else 0

