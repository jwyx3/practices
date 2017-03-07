class Solution:
    # @param {int[]} A an integer array
    # @return {long} a long integer

    # [4,2,1,3] => 3*3! + 1*2! + 0*1! + 0*0!
    #           => a*3! + b*2! + c*1!
    # for given A[i], the number of combinations are (i-1)!
    # a,b,c are numbers which A[k] < A[i], k > i
    def permutationIndex(self, A):
        result = 1 # base 1
        factor = 1
        for i in range(len(A) - 1, -1, -1):
            weight = 0
            for j in range(i + 1, len(A)):
                if A[i] > A[j]:
                    weight += 1
            result += weight * factor
            factor *= len(A) - i
        return result

