# https://leetcode.com/problems/shortest-distance-from-all-buildings/
# http://www.cnblogs.com/grandyang/p/5297683.html
# Time: O(M*N*M*N)
# Space: O(M*N)

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1
        
        m, n = len(grid), len(grid[0])
        buildings = emptys = 0
        for x in xrange(m):
            for y in xrange(n):
                if grid[x][y] == 1:
                    buildings += 1
                elif grid[x][y] == 0:
                    emptys += 1
        
        def shortest_dist_from_buildings():
            dist = [[0] * n for _ in xrange(m)]
            reach = [[0] * n for _ in xrange(m)]

            for x0 in xrange(m):
                for y0 in xrange(n):
                    if grid[x0][y0] == 1:
                        q = collections.deque([(x0, y0)])
                        visited = [[0] * n for _ in xrange(m)]
                        visited[x0][y0] = 1

                        curr_dist = 0
                        while q:
                            size = len(q)
                            for _ in xrange(size):
                                x, y = q.popleft()
                                for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and not visited[nx][ny]:
                                        visited[nx][ny] = 1
                                        reach[nx][ny] += 1
                                        dist[nx][ny] += curr_dist + 1
                                        q.append((nx, ny))
                            curr_dist += 1

            ans = float('inf')
            for x in xrange(m):
                for y in xrange(n):
                    if grid[x][y] == 0 and reach[x][y] == buildings:
                        ans = min(ans, dist[x][y])
            return ans if ans < float('inf') else -1
    
        def shortest_dist_from_emptys():
            ans = float('inf')
            for x0 in xrange(m):
                for y0 in xrange(n):
                    if grid[x0][y0] == 0:
                        total_dist = visited_buildings = 0
                        visited = [[0] * n for _ in xrange(m)]
                        visited[x0][y0] = 1
                        q = collections.deque([(x0, y0)])
                        
                        curr_dist = 0
                        while q:
                            size = len(q)
                            for _ in xrange(size):
                                x, y = q.popleft()
                                for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                                        visited[nx][ny] = 1
                                        if grid[nx][ny] == 0:
                                            q.append((nx, ny))
                                        elif grid[nx][ny] == 1:
                                            total_dist += curr_dist + 1
                                            visited_buildings += 1
                            curr_dist += 1
                        if visited_buildings == buildings:
                            ans = min(ans, total_dist)
            return ans if ans < float('inf') else -1

        if buildings <= emptys:
            return shortest_dist_from_buildings()
        else:
            return shortest_dist_from_emptys()
