class Solution:
    # @param {int} num an integer
    # @return {boolean} true if num is an ugly number or false
    def isUgly(self, num):
        bases, found = [2, 3, 5], True
        while found and num > 1:
            found = False
            for b in bases:
                if num % b == 0:
                    num /= b
                    found = True
                    break
        return num == 1

