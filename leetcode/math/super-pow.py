# https://leetcode.com/problems/super-pow
# https://leetcode.com/problems/super-pow/discuss/84466/Math-solusion-based-on-Euler's-theorem-power-called-only-ONCE-C%2B%2BJava1-line-Python

class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        # 1337 = 7 * 191
        # phi(x) = x - 1, if x is prime
        # phi(a * b) = phi(a) * phi(b)
        # b = 1140p + q
        # pow(a, b, 1337) = pow(a, b % phi(1337), 1337)
        if a % 1337 == 0: return 0
        q = 0
        for x in b:
            q = (10 * q + x) % 1140
        # corner case: 574**q % 1337 == 574. but 574**0 % 1337 == 1.
        if q == 0: q += 1140
        return pow(a, q, 1337)

### Time: O(len(b))

class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        if a % 1337 == 0:
            return 0
        res = 1
        for x in b:
            res = pow(res, 10, 1337)
            res *= pow(a, x, 1337)
        return res % 1337
