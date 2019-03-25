# https://leetcode.com/problems/smallest-integer-divisible-by-k/
# https://www.youtube.com/watch?v=AxVUCzee-XI
# Time: O(K)
# Space: O(1)

class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        # no such positive integer for N,
        # f(N) and f(M) have same remainder
        # 111111111, 1111 => f(N) - f(M) = 111110000 can be divided by K
        # 1111 can't be divided by K.
        # so 10000 can be divived by K. So k = 2 or 5 means no such positive integer
        if K % 2 == 0 or K % 5 == 0:
            return -1
        # pigeon hole, try k times from [1, k-1],
        # and it will get one duplicate
        # 1, 11, 111, etc
        rem = 0
        for i in xrange(1, K + 1):
            # rem = x % K => x = y * K + rem
            # (x * 10 + 1) % K = (y*K*10 + rem*10 + 1) % K = (rem*10 + 1) % K
            rem = (rem * 10 + 1) % K
            if rem == 0:
                return i
        return -1

