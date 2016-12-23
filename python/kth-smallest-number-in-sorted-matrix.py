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

if __name__ == '__main__':
    s = Solution()
    print s.kthSmallest([[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8]], 19), 7

