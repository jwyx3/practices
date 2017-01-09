import heapq

class Solution:
    # @param matrix: a matrix of integers
    # @param k: an integer
    # @return: the kth smallest number in the matrix
    def kthSmallest(self, matrix, k):
        # corner case:
        # 1. k > m*n
        # 2. k == 0
        x = None
        m, n = len(matrix), len(matrix[0])
        if k > m*n:
            return x
        h = []
        visited = [[0 for i in xrange(n)] for j in xrange(m)]
        # initialize
        heapq.heappush(h, (matrix[0][0], 0, 0))
        visited[0][0] = 1
        #  get k elements
        while k > 0:
            x = heapq.heappop(h)
            n_row, n_col = x[1] + 1, x[2] + 1
            if n_row < m and not visited[n_row][x[2]]:
                heapq.heappush(h, (matrix[n_row][x[2]], n_row, x[2]))
                visited[n_row][x[2]] = 1
            if n_col < n and not visited[x[1]][n_col]:
                heapq.heappush(h, (matrix[x[1]][n_col], x[1], n_col))
                visited[x[1]][n_col] = 1
            k -= 1
        return x and x[0]

    def kthSmallest0(self, matrix, k):
        def check(x):
            n, m = len(matrix), len(matrix[0])
            i, j = n - 1, 0
            existed, count = False, 0
            while i >= 0 and j < m:
                if not existed and matrix[i][j] == x:
                    existed = True
                if matrix[i][j] <= x:
                    count += (i+1)
                    j += 1
                else:
                    i -= 1
            return existed, count

        if not matrix or not matrix[0]:
            return None
        n, m = len(matrix), len(matrix[0])
        if k > m * n:
            return None

        left, right = matrix[0][0], matrix[n-1][m-1]
        while left + 1 < right:
            mid = left + (right - left) / 2
            existed, count = check(mid)
            if count < k:
                left = mid + 1
            else: # count >= k
                right = mid

        existed, count = check(left)
        if existed and count >= k:
            return left
        return right


if __name__ == '__main__':
    s = Solution()
    print s.kthSmallest([[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8]], 19), 7
    print s.kthSmallest0([[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8]], 19), 7
    print s.kthSmallest0([[1],[2],[3],[100],[101],[1000],[9999]], 5), 101
    print s.kthSmallest0([[998,1002],[998,1003],[999,1003],[1000,1003],[1000,1004]], 7), 1003

