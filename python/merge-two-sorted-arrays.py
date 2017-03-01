class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        if not A and not B:
            return []
        n, m = len(A), len(B)
        ans = [0] * (n + m)
        i, j, k = 0, 0, 0
        while i < n and j < m:
            if A[i] < B[j]:
                ans[k] = A[i]
                i += 1
            else:
                ans[k] = B[j]
                j += 1
            k += 1
        while i < n:
            ans[k] = A[i]
            k, i = k + 1, i + 1
        while j < m:
            ans[k] = B[j]
            k, j = k + 1, j + 1
        return ans

