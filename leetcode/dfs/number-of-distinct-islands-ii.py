# https://leetcode.com/problems/number-of-distinct-islands-ii/
# https://leetcode.com/problems/number-of-distinct-islands-ii/discuss/108794/Consise-C%2B%2B-solution-using-DFS-%2Bsorting-to-find-canonical-representation-for-each-island
# Time: O(R*C*log(R*C))
# Space: O(R*C)

class Solution(object):
    def numDistinctIslands2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != 1:
                return []
            grid[x][y] = 0
            ans = [(x, y)]
            for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                ans.extend(dfs(nx, ny))
            return ans
        
        def get_key(shape):
            shapes = [[] for _ in xrange(8)]
            for x, y in shape:
                shapes[0].append((x, y))
                shapes[1].append((-x, y))
                shapes[2].append((x, -y))
                shapes[3].append((-x, -y))
                shapes[4].append((y, x))
                shapes[5].append((-y, x))
                shapes[6].append((-y, -x))
                shapes[7].append((y, -x))
            
            for i, shape in enumerate(shapes):
                shape = sorted(shape)
                x0, y0 = shape[0]
                # set left-bottom point into (0, 0)
                shapes[i] = tuple((x-x0, y-y0) for x, y in shape)
            return min(shapes)

        islands = set()
        for x in xrange(m):
            for y in xrange(n):
                if grid[x][y] == 1:
                    shape = dfs(x, y)
                    islands.add(get_key(shape))
        return len(islands)
