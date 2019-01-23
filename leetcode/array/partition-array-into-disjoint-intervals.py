# https://leetcode.com/problems/partition-array-into-disjoint-intervals/
# https://leetcode.com/problems/partition-array-into-disjoint-intervals/solution/
# Time: O(N)
# Space: O(N)

class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        maxleft = [0] * N
        minright = [0] * N
        
        m = A[0]
        for i in xrange(N):
            m = maxleft[i] = max(m, A[i])
        
        m = A[-1]
        for i in xrange(N - 1, -1, -1):
            m = minright[i] = min(m, A[i])
        
        for i in xrange(1, N):
            if maxleft[i-1] <= minright[i]:
                return i
