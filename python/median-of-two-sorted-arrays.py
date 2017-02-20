class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        n, m = len(A), len(B)
        k = n + m - (n + m) / 2
        s1, s2 = self.findKth(A, B, 0, 0, k)
        # odd
        if (n + m) % 2 == 1:
            return min(A[s1:s1 + 1] + B[s2:s2 + 1])
        # even
        nums = A[s1:s1 + 2] + B[s2:s2 + 2]
        nums.sort()
        return (nums[0] + nums[1]) / 2.0

    def findKth(self, A, B, s1, s2, k):
        if k == 1:
            return (s1, s2)
        n1, n2 = k / 2, k - k / 2
        i, j = s1 + n1 - 1, s2 + n2 - 1
        if i < len(A) and j < len(B):
            if A[i] < B[j]:
                # discard first n1 elements in A
                s1, k = i + 1, n2
            else:
                # discard first n2 elements in B
                s2, k = j + 1, n1
        elif i >= len(A):
            # discard first n2 elements in B
            s2, k = j + 1, n1
        else:
            # discard first n1 elements in A
            s1, k = i + 1, n2
        # keep search first kth element
        return self.findKth(A, B, s1, s2, k)


if __name__ == '__main__':
    s = Solution()
    print s.findMedianSortedArrays([1,2,3,4,5,6], [2,3,4,5])
    print s.findMedianSortedArrays([1,2,3], [4, 5])
    print s.findMedianSortedArrays([1,3], [5])
    print s.findMedianSortedArrays([1, 2, 3], [5])
