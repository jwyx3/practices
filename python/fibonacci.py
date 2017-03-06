class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        if n <= 0:
            return -1
        fab, n = [0, 1], n - 1
        for i in range(2, n + 1):
            fab[i % 2] = fab[(i - 1) % 2] + fab[(i - 2) % 2]
        return fab[n % 2]

