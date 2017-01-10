class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        if x < 0:
            return -1
        left, right = 0, x
        while left + 1 < right:
            mid = left + (right - left) / 2
            if mid * mid == x:
                return mid
            if mid * mid < x:
                left = mid
            else:
                right = mid
        if right * right <= x:
            return right
        return left
