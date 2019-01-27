# https://leetcode.com/problems/spiral-matrix-iii/
# Time: O((max(R*C))**2)
# Space: O(R*C), size of answer array

class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        def next_round(r, c, k):
            n = 2 * k  # jump steps
            # directions: down, left, up, right
            for dr, dc in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                for _ in xrange(n):
                    r, c = r + dr, c + dc
                    if 0 <= r < R and 0 <= c < C:
                        yield r, c
        
        # max length from center to edge
        max_k = max([r0, c0, R - 1 - r0, C - 1 - c0])
        # first point the corner case
        res = [(r0, c0)]
        for k in xrange(1, max_k + 1):
            r0, c0 = r0 - 1, c0 + 1  # alway start from top-right point
            for r, c in next_round(r0, c0, k):
                res.append((r, c))
        return res
