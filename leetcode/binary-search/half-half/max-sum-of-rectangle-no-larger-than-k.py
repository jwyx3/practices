# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/
# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/discuss/83599/Accepted-C%2B%2B-codes-with-explanation-and-references
# Time: O(min(M, N)**2 * max(M, N)**2), because of insort
# Space: O(1)
# K can be negative

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        for r in xrange(m):
            for c in xrange(n):
                if c < n - 1:
                    matrix[r][c + 1] += matrix[r][c]
                if r > 0:
                    matrix[r][c] += matrix[r - 1][c]
        ans = float('-inf')  # not found
        if m <= n:
            for r1 in xrange(m):
                for r2 in xrange(r1, m):
                    psums = [0]
                    for c in xrange(n):
                        curr = matrix[r2][c] - (matrix[r1 - 1][c] if r1 > 0 else 0)
                        i = bisect.bisect_left(psums, curr - k)
                        if i < len(psums) and curr - psums[i] > ans:
                            ans = curr - psums[i]
                        bisect.insort_left(psums, curr)
        else:
            for c1 in xrange(n):
                for c2 in xrange(c1, n):
                    psums = [0]
                    for r in xrange(m):
                        curr = matrix[r][c2] - (matrix[r][c1 - 1] if c1 > 0 else 0)
                        i = bisect.bisect_left(psums, curr - k)
                        if i < len(psums) and curr - psums[i] > ans:
                            ans = curr - psums[i]
                        bisect.insort_left(psums, curr)
        return ans

