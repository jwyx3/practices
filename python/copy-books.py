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

class Solution:
    # @param pages: a list of integers
    # @param k: an integer
    # @return: an integer
    def copyBooks(self, pages, k):
        # no book
        if not pages:
            return 0
        # invalid
        if pages and k <= 0:
            return -1
        start, end = max(pages), sum(pages)
        while start + 1 < end:
            mid = start + (end - start) / 2
            # If mid is ok, then all x > mid is ok
            if self.check(pages, k, mid):
                end = mid
            else:
                start = mid
        if self.check(pages, k, start):
            return start
        return end

    # @param t: time used to copy book
    # return: boolean, whether all books can be copied within t
    @staticmethod
    def check(pages, k, t):
        total, k_tmp = 0, 0
        for page in pages:
            # this one can not read any more,
            # add one more person
            if total + page > t:
                k_tmp += 1
                total = 0
            total += page
        if total > 0:
            k_tmp += 1
        return k_tmp <= k
