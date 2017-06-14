class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.

    # Binary search
    # keep search the subarray which meet this condition:
    # A[left] < A[left+1] and A[right]  < A[right-1]
    # O(logn)
    def findPeak(self, A):
        if not A:
            return -1
        left, right, mid = 0, len(A) - 1, -1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if A[mid] < A[mid+1]:
                left = mid
            elif A[mid] < A[mid-1]:
                right = mid
            else:
                break
        return mid


# draw figure first
class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        if not A:
            return -1
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            # found peak
            if A[mid - 1] < A[mid] and A[mid + 1] < A[mid]:
                return mid
            elif A[mid - 1] < A[mid] and A[mid + 1] > A[mid]:
                start = mid
            else:
                end = mid
        return -1
