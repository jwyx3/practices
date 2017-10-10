# idea: write normal answer first
#       then swap k with j
#       to avoid process zero in B multiple times
#       construct newB
#       these are different dimensions: len(A), len(A[0]) == len(B), len(B[0])
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not A[0] or not B or not B[0]:
            return []
        result = [[0] * len(B[0]) for _ in xrange(len(A))]
        newB = []
        for i in xrange(len(B)):
            newB.append([])
            for j in xrange(len(B[0])):
                if B[i][j]:
                    newB[i].append(j)
        for i in xrange(len(A)):
            for k in xrange(len(A[0])):
                if A[i][k] != 0:
                    for j in newB[k]:
                        result[i][j] += A[i][k] * B[k][j]
        return result
