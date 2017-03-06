class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """

    # three steps reverse
    def recoverRotatedSortedArray(self, nums):
        pos = -1
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                pos = i
                break
        if pos >= 0:
            self.reverse(nums, 0, pos)
            self.reverse(nums, pos + 1, len(nums) - 1)
            self.reverse(nums, 0, len(nums) - 1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
