class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def totalOccurrence(self, A, target):
        if not A:
            return 0
        start, left, right = 0, 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if A[mid] < target:
                left = mid
            else:
                right = mid
        if A[left] == target:
            start = left
        elif A[right] == target:
            start = right
        else:
            start = -1

        end, left, right = len(A) - 1, 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if A[mid] > target:
                right = mid
            else:
                left = mid
        if A[right] == target:
            end = right
        elif A[left] == target:
            end = left
        else:
            end = -1

        return end - start + 1 if start >= 0 and end >= 0 else 0
