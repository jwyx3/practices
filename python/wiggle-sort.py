class Solution(object):
    """
    @param {int[]} nums a list of integer
    @return nothing, modify nums in-place instead
    """
    def wiggleSort(self, nums):
        if not nums or len(nums) < 2:
            return
        for i in range(1, len(nums)):
            # the relationship between two numbers only has >= or <=
            if i % 2 == 1 and nums[i] < nums[i - 1] or\
                    i % 2 == 0 and nums[i] > nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
