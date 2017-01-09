class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return 0
        n, m = len(matrix), len(matrix[0])
        ans, i, j = 0, n - 1, 0
        while i >= 0 and j < m:
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                ans += 1
                i -= 1
                j += 1
        return ans
