class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # x ^ i ^ i = x
        # 0 ^ i = i
        result = 0
        for num in nums:
            result ^= num
        for i in range(len(nums) + 1):
            result ^= i
        return result
