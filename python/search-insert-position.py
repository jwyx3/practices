class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        if not A:
            return 0
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if A[mid] >= target:
                right = mid
            else:
                left = mid + 1
        if A[right] < target:
            return right + 1
        elif A[right] >= target and A[left] < target:
            return right
        return left
