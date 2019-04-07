# https://leetcode.com/problems/bomb-enemy/
# Time: O(R*C)
# Space: O(R)

class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        rowHits, colHits, result = 0, [0] * n, 0
        for i in xrange(m):
            for j in xrange(n):
                # calculate rowHits
                if not j or grid[i][j-1] == 'W':
                    rowHits, k = 0, j
                    while k < n and grid[i][k] != 'W':
                        rowHits += grid[i][k] == 'E'
                        k += 1
                # calculate colHits[j]
                if not i or grid[i-1][j] == 'W':
                    colHits[j], k = 0, i
                    while k < m and grid[k][j] != 'W':
                        colHits[j] += grid[k][j] == 'E'
                        k += 1
                # only handle empty lot
                if grid[i][j] == '0':
                    result = max(result, rowHits + colHits[j])
        return result
                    
