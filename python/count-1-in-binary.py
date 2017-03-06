class Solution:
    # @param num: an integer
    # @return: an integer, the number of ones in num
    def countOnes(self, num):
        count = 0
        for _ in range(32):
            count += (num & 1)
            num >>= 1
        return count

