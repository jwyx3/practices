class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """
    def subarraySum(self, nums):
        if not nums:
            return [-1, -1]
        sums = [0]
        for i in range(len(nums)):
            sums.append(sums[i] + nums[i])
        h = {}
        for i in range(len(nums) + 2):
            if sums[i] in h:
                return [h[sums[i]], i - 1]
            h[sums[i]] = i
        return [-1, -1]
