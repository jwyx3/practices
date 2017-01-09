class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        n, m = len(matrix), len(matrix[0])
        left, right = 0, n - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid
        row = right
        if matrix[right][0] > target:
            row = left

        left, right = 0, m - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid
        if matrix[row][right] == target or matrix[row][left] == target:
            return True
        return False

