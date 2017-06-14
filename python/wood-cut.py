class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        def check(x, L, k):
            count = 0
            for y in L:
                count += (y / x)
            return count >= k

        if not L:
            return 0
        left, right = 1, max(L)
        while left + 1 < right:
            mid = left + (right - left) / 2
            if check(mid, L, k):
                left = mid
            else:
                right = mid - 1
        if check(right, L, k):
            return right
        if check(left, L, k):
            return left
        return 0

class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    @staticmethod
    def check(L, k, cut_len):
        n = 0
        for wood_len in L:
            n += (wood_len / cut_len)
        return n >= k

    def woodCut(self, L, k):
        if not L or k > sum(L):
            return 0
        start, end = 0, max(L)
        while start + 1 < end:
            mid = start + (end - start) / 2
            if self.check(L, k, mid):
                start = mid
            else:
                end = mid
        if self.check(L, k, end):
            return end
        elif self.check(L, k, start):
            return start
        return 0
