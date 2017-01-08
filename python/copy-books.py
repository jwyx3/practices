class Solution:
    # @param pages: a list of integers
    # @param k: an integer
    # @return: an integer
    def copyBooks(self, pages, k):
        # can k persons copy books within x minutes
        def check(x):
            total, kt = 0, 0
            for p in pages:
                # current person cannot copy any more
                # add one more person
                if total + p > x:
                    kt += 1
                    total = 0
                total += p
            return (kt + (0 if total == 0 else 1)) <= k

        # no books
        if not pages:
            return 0
        # has books but no person
        if pages and k <= 0:
            return -1

        left, right = 0, 0
        for p in pages:
            # the time of book with max pages
            left = max(left, p)
            # the total time to copy books for one person
            right += p

        while left + 1 < right:
            mid = left + (right - left) / 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        if check(left):
            return left
        return right
