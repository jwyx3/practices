class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        if not A:
            return [-1, -1]
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if A[mid] < target:
                left = mid + 1
            else:
                right = mid
        start = -1
        if A[left] == target:
            start = left
        elif A[right] == target:
            start = right

        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if A[mid] > target:
                right = mid - 1
            else:
                left = mid
        end = -1
        if A[right] == target:
            end = right
        elif A[left] == target:
            end = left

        return [start, end]

if __name__ == '__main__':
    s = Solution()
    print s.searchRange([1], 1), "#", "[0, 0]"
