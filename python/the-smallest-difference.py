class Solution:
    # @param A, B: Two lists of integer
    # @return: An integer
    def smallestDifference(self, A, B):
        if not A or not B:
            return 0
        A.sort()
        B.sort()

        ans, i, j = sys.maxint, 0, 0
        while i < len(A) and j < len(B):
            ans = min(ans, abs(A[i] - B[j]))
            if A[i] < B[j]:
                i += 1
            else:
                j += 1
        return ans
