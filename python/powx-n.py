class Solution:
    # @param {double} x the base number
    # @param {int} n the power number
    # @return {double} the result

    # divide and conquer
    # time: O(logn)
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        negative = False
        if n < 0:
            negative = True
            n = -n
        k = n / 2
        rest = n - k * 2
        r1 = self.myPow(x, k) # O(n/2)
        r2 = self.myPow(x, rest) # O(1)
        if negative:
            return 1.0 / (r1 * r1 * r2)
        return r1 * r1 * r2
