# https://leetcode.com/problems/score-after-flipping-matrix/
# https://leetcode.com/problems/score-after-flipping-matrix/discuss/143722/C%2B%2BJavaPython-Easy-and-Concise
# Time: O(R*C)
# Space: O(1)
# toggle rows first, because first column should be 1
# toggle cols to get more 1s

class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        R, C = len(A), len(A[0])
        res = R * (1 << (C - 1))
        for c in xrange(1, C):
            ones = sum(A[r][0] == A[r][c] for r in xrange(R))
            res += max(ones, R - ones) * (1 << (C - 1 - c))
        return res
