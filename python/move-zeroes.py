class Solution:
    # @param {int[]} nums an integer array
    # @return nothing, do this in-place

    # two pointers with same direction
    def moveZeroes(self, nums):
        # Write your code here
        if not nums:
            return
        left, right = 0, 0
        while right < len(nums):
            # right is the index of first non-zero element
            if nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

