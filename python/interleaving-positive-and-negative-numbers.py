class Solution:
    """
    @param A: An integer array.
    @return nothing
    """

    # O(n): partition first, then interleave
    def rerange(self, A):
        if not A and len(A) <= 1:
            return
        # partition
        left, right = 0, len(A) - 1
        while left <= right:
            # find first element > 0
            while left <= right and A[left] < 0:
                left += 1
            # find last element < 0
            while left <= right and A[right] > 0:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        # swap
        neg_count, count = left, len(A)
        start, end = 0, len(A) - 1
        if count % 2:
            if neg_count > count - neg_count:
                start += 1
            else:
                end -= 1
        flag = True
        while start < end:
            if flag:
                A[start], A[end] = A[end], A[start]
            flag = not flag
            start += 1
            end -= 1


if __name__ == '__main__':
    s = Solution()
    A = [-13,-8,-12,-15,-14,35,7,-1,11,27,10,-7,-12,28,18]
    s.rerange(A)
    print A
