# https://leetcode.com/problems/binary-subarrays-with-sum/
# https://leetcode.com/problems/binary-subarrays-with-sum/solution/

class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        sum_lo = sum_hi = 0
        i_lo = i_hi = 0
        res = 0
        for j, x in enumerate(A):
            sum_lo += x
            while i_lo < j and sum_lo > S:
                sum_lo -= A[i_lo]
                i_lo += 1
            sum_hi += x
            while i_hi < j and (sum_hi > S or sum_hi == S and not A[i_hi]):
                sum_hi -= A[i_hi]
                i_hi += 1
            if sum_lo == S:
                res += i_hi - i_lo + 1
        return res
