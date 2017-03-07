class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        sign = 1
        if n < 0:
            sign = -1
            n = -n
        ans, overflow = 0, 0xffffffff / 10
        while n > 0:
            if ans > overflow:
                ans = 0
                break
            ans = ans * 10 + n % 10
            n /= 10
        return sign * ans
