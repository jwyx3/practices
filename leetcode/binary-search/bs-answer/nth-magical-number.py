# https://leetcode.com/problems/nth-magical-number/
# https://zxi.mytechroad.com/blog/math/leetcode-878-nth-magical-number/
# Time: O(log(10**9 * min(A, B)))
# Space: O(1)

class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        def gcd(a, b):
            if a % b == 0:
                return b
            return gcd(b, a % b)
        
        # the number <= mid divisible by either A or B
        def check(mid):
            return mid / A + mid / B - mid / (A * B / gcd(A, B))
        
        MOD = 10 ** 9 + 7
        lo, hi = min(A, B), 10**9 * min(A, B) + 1
        while lo < hi:
            mid = (lo + hi) / 2
            if check(mid) >= N:
                hi = mid
            else:
                lo = mid + 1
        return lo % MOD
