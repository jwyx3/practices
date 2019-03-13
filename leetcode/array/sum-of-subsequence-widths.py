# https://leetcode.com/problems/sum-of-subsequence-widths/
# https://leetcode.com/problems/sum-of-subsequence-widths/discuss/161267/C%2B%2BJava1-line-Python-Sort-and-One-Pass
# Time: O(NlogN)
# Space: O(1)
# order is not important!

class Solution(object):
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        MOD = 10**9 + 7
        ans, n = 0, len(A)
        for i in xrange(n):
            ans += A[i] * (1 << i)  # as max
            ans -= A[i] * (1 << (n - 1 - i))  # as min
        return ans % MOD
