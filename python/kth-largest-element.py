import random

class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        if not A or len(A) < k or k <= 0:
            return 0
        return self.helper(A, 0, len(A) - 1, len(A) - k)

    # k is the index of kth largest element
    def helper(self, A, left, right, k):
        if left == right:
            return A[left]
        # random
        idx = random.randint(left, right)
        A[left], A[idx] = A[idx], A[left]
        # get the index of pivot
        pos = self.partition(A, left, right)
        # if it's kth largest element
        if pos == k:
            return A[pos]
        elif pos < k:
            return self.helper(A, pos + 1, right, k)
        else:
            return self.helper(A, left, pos - 1, k)

    def partition(self, A, left, right):
        pivot = A[left]
        while left < right:
            while left < right and A[right] >= pivot:
                right -= 1
            A[left] = A[right]
            while left < right and A[left] <= pivot:
                left += 1
            A[right] = A[left]
        A[left] = pivot
        return left

if __name__ == '__main__':
    s = Solution()
    print s.kthLargestElement(10, [1,2,3,4,5,6,8,9,10,7]), '#', '1'
    print s.kthLargestElement(3, [9,3,2,4,8]), '#', '4'
