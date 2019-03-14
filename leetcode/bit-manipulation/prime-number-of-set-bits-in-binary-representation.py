# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/
# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/solution/
# Time: O(NlogM), M = 10**6
# Space: O(1)

class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        ans = 0
        # R = [1,10**6]
        primes = {2,3,5,7,11,13,17,19}
        for x in xrange(L, R + 1):
            bits = bin(x).count('1')
            if bits in primes:
                ans += 1
        return ans
