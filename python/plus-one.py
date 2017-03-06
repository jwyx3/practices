class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        accum = 0
        for i in range(len(digits) - 1, -1, -1):
            s = digits[i] + 1
            digits[i] = s % 10
            accum = s / 10
            if accum == 0:
                break
        if accum == 1:
            digits.insert(0, 1)
        return digits
