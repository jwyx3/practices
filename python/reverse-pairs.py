class Solution:
    # @param {int[]} A an array
    # @return {int} total of reverse pairs

    # merge sort
    def reversePairs(self, A):
        return self.mergesort(A, 0, len(A) - 1)

    def mergesort(self, A, start, end):
        if start >= end:
            return 0
        mid = start + (end - start) / 2
        result = 0
        result += self.mergesort(A, start, mid)
        result += self.mergesort(A, mid + 1, end)
        result += self.merge(A, start, mid, end)
        return result

    def merge(self, A, start, mid, end):
        result = 0
        left, right, index = start, mid + 1, 0
        temp = [0 for _ in range(end - start + 1)]
        while left <= mid and right <= end:
            if A[left] <= A[right]:
                temp[index] = A[left]
                left += 1
            else:
                temp[index] = A[right]
                result += mid - left + 1
                right += 1
            index += 1
        while left <= mid:
            temp[index] = A[left]
            left += 1
            index += 1
        while right <= end:
            temp[index] = A[right]
            right += 1
            index += 1
        for i in range(len(temp)):
            A[start + i] = temp[i]
        return result
