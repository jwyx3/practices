# https://leetcode.com/problems/pacific-atlantic-water-flow/
# Time: O(m*n)
# Space: O(m*n)

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []
    
        m, n = len(matrix), len(matrix[0])
        p_reach = [[0] * n for _ in xrange(m)]
        a_reach = [[0] * n for _ in xrange(m)]
        
        def dfs(x, y, reach):
            if reach[x][y]:
                return
            reach[x][y] = 1
            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if (0 <= nx < m and 0 <= ny < n and not reach[nx][ny] and
                        matrix[nx][ny] >= matrix[x][y]):
                    dfs(nx, ny, reach)
        
        # Pacific
        for y in xrange(n):
            dfs(0, y, p_reach)
        for x in xrange(1, m):
            dfs(x, 0, p_reach)
        
        # Atlantic
        for y in xrange(n):
            dfs(m - 1, y, a_reach)
        for x in xrange(m - 1):
            dfs(x, n - 1, a_reach)

        return [[x, y] for x in xrange(m) for y in xrange(n) if p_reach[x][y] + a_reach[x][y] == 2]

