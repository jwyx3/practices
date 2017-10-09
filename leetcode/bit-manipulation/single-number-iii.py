class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x = 0
        # find the distinct bit of these two numbers
        for num in nums:
            x ^= num
        # extract the last bit
        bit = x & -x
        # divide to two groups and apply XOR
        result = [0, 0]
        for num in nums:
            if num & bit:
                result[0] ^= num
            else:
                result[1] ^= num
        return result

