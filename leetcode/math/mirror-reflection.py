# https://leetcode.com/problems/mirror-reflection/
# https://leetcode.com/problems/mirror-reflection/solution/
# https://leetcode.com/problems/mirror-reflection/discuss/141773/C%2B%2BJavaPython-1-line-without-using-any-package-or
# Time: O(logN) ?? gcd
# Space: O(1)

class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        # first point (kp, kq) with kq % p == 0
        # assume p = x*gcd, q = y*gcd
        # k is smallest integer, so k = x = p / gcd
        # based on odd/even of kp/p and kq/p, i.e. p/gcd, q/gcd
        # p/gcd odd, q/gcd odd -> 1
        # p/gcd odd, q/gcd even -> 0
        # p/gcd even, q/gcd odd -> 2
        from fractions import gcd
        d = gcd(p, q)
        p = (p / d) % 2
        q = (q / d) % 2
        return 1 - p + q
