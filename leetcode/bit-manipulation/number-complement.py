class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        mask = ~0 # 使用~0而不是0xffffffff，保证所有32位之前的都为1
        while num & mask: # 找到最高位的1
            # e.g. 0xfffff0000
            mask <<= 1
        return ~mask & ~num
