# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/
# https://zxi.mytechroad.com/blog/greedy/leetcode-995-minimum-number-of-k-consecutive-bit-flips/
# Time: O(N)
# Space: O(N)

class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # flipped[i]: 1 if flip at i
        # flipped[i-K] is close event
        N = len(A)
        flipped = [0] * N
        ans = flip = 0
        for i in xrange(N):
            if i >= K:
                flip ^= flipped[i-K]
            if (A[i] ^ flip) == 0:
                if i + K > N:
                    return -1
                flipped[i] = 1
                flip ^= 1
                ans += 1
        return ans
