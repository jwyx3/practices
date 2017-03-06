class Solution:
    # @param n a integer
    # @return ans a integer

    # numbers of prime factor 5 in 1 ... n
    # because number of prime factor 2 is more than 5
    # the number of tailing zeros are number of pair of 2 and 5
    # E.g. n =  11
    # n/5 => number of numbers which has one 5
    # n/25 => number of numbers which has two 5
    # ...
    def trailingZeros(self, n):
        ans = 0
        while n:
            n /= 5
            ans += n
        return ans
