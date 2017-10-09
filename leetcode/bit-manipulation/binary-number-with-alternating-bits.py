class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n:
            bits = n & 0x3
            if not ((bits >> 1) ^ (bits & 0x1)):
                return False
            n >>= 1 # for adjacent bits
        return True
