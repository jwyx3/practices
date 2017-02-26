class Solution:
    # @param k & A a integer and an array
    # @return ans a integer

    # time O(n), space O(1): quick select
    def kthLargestElement(self, k, A):
        if not A or len(A) < k:
            return -1
        return self.quickselect(A, 0, len(A) - 1, k)

    def quickselect(self, A, start, end, k):
        if start == end:
            return A[start]

        # partition
        left, right = start, end
        mid = left + (right - left) / 2
        pivot, A[mid] = A[mid], A[left]
        while left < right:
            # find last element > pivot
            while left < right and A[right] <= pivot:
                right -= 1
            A[left] = A[right]
            # find first element < pivot
            while left < right and A[left] >= pivot:
                left += 1
            A[right] = A[left]
        A[left] = pivot

        # split
        if left + 1 == k:
            return A[left]
        elif left + 1 > k:
            return self.quickselect(A, start, left - 1, k)
        else:
            return self.quickselect(A, left + 1, end, k)
