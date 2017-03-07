from collections import defaultdict


class Solution:
    # @param {string} A a string
    # @param {string} B a string
    # @return {boolean} a boolean

    # hash
    def stringPermutation(self, A, B):
        if A is None or B is None or len(A) != len(B):
            return False
        d = defaultdict(int)
        for c in A:
            d[c] += 1
        for c in B:
            if d[c] == 0:
                return False
            d[c] -= 1
        return True

