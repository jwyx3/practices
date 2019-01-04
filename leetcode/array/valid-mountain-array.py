# https://leetcode.com/problems/valid-mountain-array/
# https://leetcode.com/problems/valid-mountain-array/solution/

class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        N = len(A)
        i = 0
        
        # walk up
        while i + 1 < N and A[i] < A[i + 1]:
            i += 1
        
        if i == 0 or i == N - 1:
            return False
        
        # walk down
        while i + 1 < N and A[i] > A[i + 1]:
            i += 1
            
        return i == N - 1
