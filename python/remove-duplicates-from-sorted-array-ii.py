class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    # [1,1,1,2,2,3]
    def removeDuplicates(self, A):
        if not A:
            return 0
        # curt is the last valid index
        curt, count = 0, 1
        for i in range(1, len(A)):
            if A[curt] == A[i]:
                if count >= 2:
                    continue
                count += 1
            else:
                count = 1
            curt += 1
            A[curt] = A[i]
        return curt + 1

