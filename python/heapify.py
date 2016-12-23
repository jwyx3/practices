class Solution:
    def shiftdown(self, idx, A):
        while(idx < len(A)):
            left, right, smallest = 2 * idx + 1, 2 * idx + 2, idx
            if left < len(A) and A[left] < A[smallest]:
                smallest = left
            if right < len(A) and A[right] < A[smallest]:
                smallest = right
            if smallest == idx:
                break
            A[idx], A[smallest] = A[smallest], A[idx]
            idx = smallest


    # @param A: Given an integer array
    # @return: void
    def heapify(self, A):
        for idx in reversed(xrange(len(A) / 2)):
            self.shiftdown(idx, A)


if __name__ == '__main__':
    s = Solution()
    A = [3,2,1,4,5]
    s.heapify(A)
    print A

