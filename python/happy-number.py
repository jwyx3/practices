class Solution:
    # @param {int} n an integer
    # @return {boolean} true if this is a happy number or false

    # hash
    def isHappy(self, n):
        d = {}
        while n != 1 and n not in d:
            d[n] = 1
            n = sum([int(num) * int(num) for num in list(str(n))])
        return n == 1
