class Solution:
    # @param n: an integer
    # @param times: a list of integers
    # @return: an integer
    def copyBooksII(self, n, times):
        def check(x):
            nt = 0
            for t in times:
                nt += (x / t)
            return nt >= n

        if n == 0:
            return 0
        if not times:
            return -1

        # right: the slowest one copy all books
        left, right = 0, n * max(times)

        while left + 1 < right:
            mid = left + (right - left) / 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        if check(left):
            return left
        return right
