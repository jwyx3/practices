# https://leetcode.com/problems/transpose-matrix/
# https://leetcode.com/problems/transpose-matrix/solution/
# Time: O(R*C)
# Space: O(R*C), size of ans

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        R, C = len(A), len(A[0])
        ans = [[0] * R for _ in xrange(C)]
        for r in xrange(R):
            for c in xrange(C):
                ans[c][r] = A[r][c]
        return ans
        
