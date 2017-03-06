class Solution:
    # @param {string} a a number
    # @param {string} b a number
    # @return {string} the result
    def addBinary(self, a, b):
        result, accum = '', 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0:
            ai = int(a[i]) if i >= 0 else 0
            bj = int(b[j]) if j >= 0 else 0
            s = ai + bj + accum
            result = str(s % 2) + result
            accum = s / 2
            i -= 1
            j -= 1
        if accum == 1:
            result = '1' + result
        return result
