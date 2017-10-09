# idea:
# * one 1 bit
# * the position of 1 bit should be power of four
# * n > 0

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        # 0x55555555所有power of four对应bit所在的位置
        return num & 0x55555555 != 0 and not num & (num - 1)

    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        # 4**n - 1 = 4 * 4**(n-1) - 1 = 3 * 4**(n-1) + 4**(n-1) - 1
        #          = ... + 4**0 - 1
        # ...部分一定能被3整除, 4**0 - 1 == 0
        # 先判断是否为2**n, 然后判断是否能被3整除
        return not (num & (num - 1)) and (num - 1) % 3 == 0
