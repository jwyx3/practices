# check whether one number is power of two
# * only one bit is 1
# * number is > 0

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        # is 0 after removing one bit
        return not (n & (n - 1))
