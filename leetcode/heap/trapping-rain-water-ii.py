# https://leetcode.com/problems/trapping-rain-water-ii/
# http://www.cnblogs.com/grandyang/p/5928987.html
# greedy: heap + BFS
# from boundery and height of one cell is determined by its lowest neighbors
# Time: O(M*Nlog(M*N))
# Space: O(M*N)

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in xrange(m)]
        ans, min_h, q = 0, 0, []
        
        for i in xrange(m):
            for j in (0, n - 1):
                heapq.heappush(q, (heightMap[i][j], i * n + j))
                visited[i][j] = True
        
        for i in (0, m - 1):
            for j in xrange(n):
                heapq.heappush(q, (heightMap[i][j], i * n + j))
                visited[i][j] = True
        
        while q:
            h, idx = heapq.heappop(q)
            i, j = idx / n, idx % n
            min_h = max(min_h, h)
            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if ni < 0 or ni >= m or nj < 0 or nj >= n or visited[ni][nj]:
                    continue
                visited[ni][nj] = True
                if heightMap[ni][nj] < min_h:
                    ans += min_h - heightMap[ni][nj]
                heapq.heappush(q, (heightMap[ni][nj], ni * n + nj))

        return ans
