class Solution:
    # @param nums: a list of integers
    # @return: nothing

    # partition
    # O(n): in-place
    def partitionArray(self, nums):
        if not nums or len(nums) <= 1:
            return
        left, right = 0, len(nums) - 1
        while left <= right:
            # find first element which is even
            while left <= right and nums[left] % 2:
                left += 1
            # find last element which is odd
            while left <= right and not nums[right] % 2:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
