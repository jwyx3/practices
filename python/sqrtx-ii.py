class Solution:
    # @param {double} x a double
    # @return {double} the square root of x
    def sqrt(self, x):
        left, mid, right = 0.0, 0.0, x
        if x < 1.0:
            right = 1.0
        while right - left > 1e-12:
            mid = (left + right) / 2.0
            if mid * mid > x:
                right = mid
            else:
                left = mid
        return left
