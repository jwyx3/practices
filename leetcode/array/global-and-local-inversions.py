# https://leetcode.com/problems/global-and-local-inversions/
# Time: O(N)
# Space: O(1)

class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # if j <= i - 2, max(A[j]) > A[i] not ideal
        max_x = -1
        for i, x in enumerate(A):
            if i >= 2:
                max_x = max(max_x, A[i-2])
            if max_x > x:
                return False
        return True
        
