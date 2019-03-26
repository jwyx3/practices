# https://leetcode.com/problems/cut-off-trees-for-golf-event/
# https://leetcode.com/problems/cut-off-trees-for-golf-event/solution/
# Time: O(M*N * M*N)
# Space: O(M*N)
# TLE!!!

class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        m, n = len(forest), len(forest[0])
        nodes = sorted([
            (x, r, c) for r, row in enumerate(forest)
            for c, x in enumerate(row) if x > 1])
        
        def bfs(sx, sy, tx, ty):
            q = collections.deque([(sx, sy)])
            visited = {(sx, sy)}
            steps = 0
            while q:
                size = len(q)
                for _ in xrange(size):
                    x, y = q.popleft()
                    if x == tx and y == ty:
                        return steps
                    for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                        if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and forest[nx][ny]:
                            visited.add((nx, ny))
                            q.append((nx, ny))
                steps += 1
            return -1
        
        sx = sy = ans = 0
        for _, tx, ty in nodes:
            steps = bfs(sx, sy, tx, ty)
            if steps < 0:
                return -1
            ans += steps
            sx, sy = tx, ty
        return ans
        
# A* search

