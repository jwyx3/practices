class Solution:
    # @param {int[][]} matrix an integer matrix
    # @return {int[][]} the coordinate of the left-up and right-down number

    def submatrixSum(self, matrix):
        if not matrix or not matrix[0]:
            return None
        n, m = len(matrix), len(matrix[0])
        sums = [[0 for y in xrange(m+1)] for x in xrange(n+1)]
        # 得到每列的前缀和
        for y in xrange(1, m+1):
            for x in xrange(1, n+1):
                sums[x][y] = sums[x-1][y] + matrix[x-1][y-1]
        for x in xrange(1, n+1):
            for y in xrange(1, m+1):
                sums[x][y] += sums[x][y-1]
        # 将两行之间所有行每列的和看成一维数组
        for x1 in xrange(1, n+1):
            for x2 in xrange(x1, n+1):
                h = {}
                for y in xrange(0, m+1):
                    sums_x = sums[x2][y] - sums[x1-1][y]
                    if sums_x in h:
                        return [h[sums_x], (x2-1, y-1)]
                    h[sums_x] = (x1-1, y) # y = y-1+1
        return None
