# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/discuss/252242/JavaPython-Find-Intersection-of-Dominos
# Time: O(N)
# Space: O(1)

class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        cands = set([A[0], B[0]])
        for i in xrange(1, n):
            cands &= set([A[i], B[i]])
        if not cands:
            return -1
        # handle both one or two candidate
        x = cands.pop()
        return min(n - A.count(x), n - B.count(x))
