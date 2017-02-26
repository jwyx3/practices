class Solution:
    # @param nums, an array of integer
    # @param target, an integer
    # @return an integer
    def twoSum2(self, nums, target):
        if not nums or len(nums) < 2:
            return 0
        nums.sort()
        count, left, right = 0, 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] > target:
                count += (right - left)
                right -= 1
            else:
                left += 1
        return count
