import sys

class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def closestNumber(self, A, target):
        if not A:
            return -1
        left, right = 0, len(A) - 1
        min_diff = sys.maxint
        while left + 1 < right:
            mid = left + (right - left) / 2
            if A[mid] == target:
                return mid
            if A[mid] > target:
                right = mid
            else:
                left = mid
        min_diff, ans = abs(A[right] - target), right
        if abs(A[left] - target) < min_diff:
            ans = left
        return ans

