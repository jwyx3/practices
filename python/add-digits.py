class Solution:
    # @param {int} num a non-negative integer
    # @return {int} one digit

    # num = A[0]*10^n + A[1]*10^(n-1) + ... + A[n]
    # A[i]*10^(n-i) % 9 = A[i]
    # => num % 9 = (A[0] + A[1] + ... + A[n]) % 9
    #            = num1 % 9
    #            = (B[0] + B[1] + ... + B[m]) % 9
    #            = num2 % 9
    def addDigits(self, num):
        if num == 0:
            return 0
        ans = num % 9
        if ans == 0:
            return 9
        return ans

