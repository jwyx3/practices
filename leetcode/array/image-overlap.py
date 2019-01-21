# https://leetcode.com/problems/image-overlap/
# https://leetcode.com/problems/image-overlap/solution/
# https://leetcode.com/problems/image-overlap/discuss/130623/C%2B%2BJavaPython-Straight-Forward
# Time: O(N**4)
# Space: O(N**2)
# handle sparse matrix
# 1. for each overlap, get delta
# 2. for each delta, get overlap

class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        N = len(A)
        A1 = [(i/N, i%N) for i in xrange(N*N) if A[i/N][i%N]]
        B1 = [(i/N, i%N) for i in xrange(N*N) if B[i/N][i%N]]
        count = collections.Counter((xa - xb, ya - yb) for xa, ya in A1 for xb, yb in B1)
        return max(count.values()) if count else 0
