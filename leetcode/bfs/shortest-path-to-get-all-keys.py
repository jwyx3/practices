# https://leetcode.com/problems/shortest-path-to-get-all-keys/
# https://zxi.mytechroad.com/blog/searching/leetcode-864-shortest-path-to-get-all-keys/
# Time: O(M*N*2**6)
# Space: O(M*N*2**6)

class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1
        m, n = len(grid), len(grid[0])
        # state: x << 16 | y << 8 | 2**6
        # one cell can be visited multiple times
        all_keys = start = 0
        for r in xrange(m):
            for c in xrange(n):
                if grid[r][c] == '@':
                    start = (r << 16) | (c << 8)
                elif 'a' <= grid[r][c] <= 'f':
                    all_keys |= 1 << (ord(grid[r][c]) - ord('a'))
        
        q = collections.deque([start])
        visited = set([start])
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        steps = 0
        
        while q:
            size = len(q)
            for _ in xrange(size):
                state = q.popleft()
                x, y, keys = (state >> 16) & 0xff, (state >> 8) & 0xff, state & 0xff
                if keys == all_keys:
                    return steps
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] == '#':
                        continue
                    if 'A' <= grid[nx][ny] <= 'F' and not (keys & (1 << ord(grid[nx][ny]) - ord('A'))):
                        continue
                    if 'a' <= grid[nx][ny] <= 'f':
                        nstate = (nx << 16) | (ny << 8) | (keys | (1 << ord(grid[nx][ny]) - ord('a')))
                    else:
                        nstate = (nx << 16) | (ny << 8) | keys
                    if nstate in visited:
                        continue
                    q.append(nstate)
                    visited.add(nstate)
            steps += 1
        return -1
