class Solution:
    """
    @param A: Given an integers array A
    @return: An integer array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    # [1, 2, 3]
    def productExcludeItself(self, A):
        n, B = len(A), [] # => n = 3
        suffix = [0 for _ in range(n + 1)]
        suffix[n] = 1 # => [0, 0, 0, 1]
        for i in range(n - 1, 0, -1):
            suffix[i] = suffix[i + 1] * A[i] # => [6, 6, 3, 1]
        tmp = 1
        for i in range(n):
            B.append(tmp * suffix[i + 1]) # => [6, 3, 2]
            tmp *= A[i]
        return B
