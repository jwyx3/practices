# https://leetcode.com/problems/number-of-corner-rectangles/
# https://leetcode.com/problems/number-of-corner-rectangles/solution/
# We ask the question: for each additional row, how many more rectangles are added?
# Time: O(R*C*C)
# Space: O(C*C)

class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R, C = len(grid), len(grid[0])
        res = 0
        count = collections.Counter()
        for r in xrange(R):
            for i in xrange(C-1):
                if grid[r][i]:  # handle this for sparse matrix to avoid TLE
                    for j in xrange(i+1, C):
                        if grid[r][j]:
                            res += count[i, j]
                            count[i, j] += 1
        return res

# TODO: hybrid
# https://leetcode.com/problems/number-of-corner-rectangles/solution/ 
