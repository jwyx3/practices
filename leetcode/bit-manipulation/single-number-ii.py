class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, MAX_INT = 0, 0x7fffffff
        for i in range(32):
            bit = 0
            for num in nums:
                bit += (num >> i) & 1
            bit %= 3
            result |= bit << i
        # 如果为负数需要模拟32位
        if result > MAX_INT:
            result = (~0 << 31) | result
        return result
