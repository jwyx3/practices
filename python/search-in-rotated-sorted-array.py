class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        if not A:
            return -1
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if A[mid] == target:
                return mid
            if A[left] < A[mid]:
                # keep find increasing part
                if A[left] <= target and target <= A[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if A[mid] <= target and target <= A[right]:
                    left = mid
                else:
                    right = mid
        if A[left] == target:
            return left
        if A[right] == target:
            return right
        return -1

if __name__ == '__main__':
    s = Solution()
    print s.search([1, 2, 3], 1), '#', '0'


