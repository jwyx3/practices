class Solution:
    # @param nums {int[]} an array of integer
    # @param target {int} an integer
    # @return {int} an integer
    def twoSum6(self, nums, target):
        if not nums or len(nums) < 2:
            return 0
        nums.sort()
        count, left, right = 0, 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                count += 1
                left += 1
                right -= 1
                # remove duplicate
                while left < right and nums[left - 1] == nums[left]:
                    left += 1
                while left < right and nums[right + 1] == nums[right]:
                    right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return count
