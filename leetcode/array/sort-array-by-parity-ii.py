# https://leetcode.com/problems/sort-array-by-parity-ii/

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A or len(A) < 1:
            return A
        N = len(A)
        i, j = 0, 1
        while i < N and j < N:
            while i < N and A[i] & 1 == 0:
                i += 2
            while j < N and A[j] & 1 == 1:
                j += 2
            if i < N and j < N:
                A[i], A[j] = A[j], A[i]
                i += 2
                j += 2
        return A
