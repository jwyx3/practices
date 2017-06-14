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

# no duplicate
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        if not A:
            return -1
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            # found the element
            if A[mid] == target:
                return mid
            # check red line
            elif A[start] < A[mid]:
                # check inceasing part
                if A[start] <= target and target <= A[mid]:
                    end = mid
                else:
                    start = mid
            # check green line
            else:
                # check increasing part
                if A[mid] <= target and target <= A[end]:
                    start = mid
                else:
                    end = mid
        if A[start] == target:
            return start
        elif A[end] == target:
            return end
        return -1


if __name__ == '__main__':
    s = Solution()
    print s.search([1, 2, 3], 1), '#', '0'


