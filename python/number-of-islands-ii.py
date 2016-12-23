class Solution:
    # @param {int} n an integer
    # @param {int} m an integer
    # @param {Pint[]} operators an array of point
    # @return {int[]} an integer array
    def numIslands2(self, n, m, operators):
        father = [[0 for i in xrange(m)] for j in xrange(n)]
        grid = [[0 for i in xrange(m)] for j in xrange(n)]
        count = 0

        def find(a):
            if father[a.x][a.y] == 0:
                return a
            father[a.x][a.y] = find(father[a.x][a.y])
            return father[a.x][a.y]

        def union(a, b, count):
            ra = find(a)
            rb = find(b)
            if ra.x != rb.x or ra.y != rb.y:
                father[ra.x][ra.y] = rb
                count -= 1
            return count

        ans = []
        delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for op in operators:
            count += 1
            grid[op.x][op.y] = 1
            for dx, dy in delta:
                nx, ny = op.x + dx, op.y + dy
                # If adjacent nodes are valid islands
                if nx >= 0 and nx < n and ny >= 0 and ny < m and grid[nx][ny]:
                    count = union(Point(op.x, op.y), Point(nx, ny), count)
            ans.append(count)
        return ans
