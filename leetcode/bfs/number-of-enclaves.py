# https://leetcode.com/problems/number-of-enclaves/
# coloring problem

class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if not A or not A[0]:
            return 0
        
        m, n = len(A), len(A[0])
        
        def bfs(x, y):
            q = collections.deque([(x, y)])
            while q:
                x, y = q.popleft()
                for nx, ny in ((x+1, y), (x-1, y), (x, y-1), (x, y+1)):
                    if nx < 0 or nx >= m or ny < 0 or ny >= n or A[nx][ny] != 1:
                        continue
                    A[nx][ny] = 2
                    q.append((nx, ny))
        
        for x in xrange(m):
            for y in (0, n-1):
                if A[x][y] == 1:
                    A[x][y] = 2
                    bfs(x, y)
        for x in (0, m-1):
            for y in xrange(n):
                if A[x][y] == 1:
                    A[x][y] = 2
                    bfs(x, y)
        ans = 0
        for x in xrange(m):
            for y in xrange(n):
                if A[x][y] == 1:
                    ans += 1
        return ans
