class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        if not A:
            return 0
        start = 0
        for i in range(len(A)):
            if i > 0 and A[i] == A[i - 1]:
                continue
            A[start] = A[i]
            start += 1
        return start
