# https://leetcode.com/problems/consecutive-numbers-sum/
# Time: O(sqrt(N))
# Space: o(1)

class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        # consecutive positive integers must be
        # N = x+1 + x+2 + ... + x+k, x>=0, k>=1
        # 2N = k(2kx + k + 1), let b = 2kx+k+1
        # If k is odd, b is even
        # If k is even, b is odd
        # obviously, k < b and 1 <= k <= (2N)**0.5
        k, N, maxk = 1, 2*N, (2*N)**.5
        res = 0
        for k in xrange(1, int(maxk) + 1):
            b, rem = divmod(N, k)
            if not rem and (k & 1) ^ (b & 1):
                res += 1 
        return res
