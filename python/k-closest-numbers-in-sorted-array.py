class Solution:
    # @param {int[]} A an integer array
    # @param {int} target an integer
    # @param {int} k a non-negative integer
    # @return {int[]} an integer array
    def kClosestNumbers(self, A, target, k):
        if not A or len(A) < k:
            return []
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if A[mid] == target:
                left = right = mid
                break
            if A[mid] > target:
                right = mid
            else:
                left = mid
        start = right
        if abs(A[left] - target) <= abs(A[right] - target):
            start = left
        ans, i, j = [], start, start + 1
        while k >= 1:
            if i >= 0 and j < len(A):
                if abs(A[i] - target) <= abs(A[j] - target):
                    ans.append(A[i])
                    i -= 1
                else:
                    ans.append(A[j])
                    j += 1
            elif j < len(A):
                ans.append(A[j])
                j += 1
            else:
                ans.append(A[i])
                i -= 1
            k -= 1
        return ans
