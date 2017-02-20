class Solution:
    # @param nums {int[]} an array of integer
    # @param target {int} an integer
    # @return {int} an integer
    def twoSum6(self, nums, target):
        # Write your code here
        if not nums or len(nums) < 2:
            return 0
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        while left < right:
            nums_sum = nums[left] + nums[right]
            if nums_sum == target:
                count += 1
                left += 1
                right -= 1
                # remove dup
                while left < right and nums[left - 1] == nums[left]:
                    left += 1
                while left < right and nums[right + 1] == nums[right]:
                    right -= 1
            elif nums_sum > target:
                right -= 1
            else:
                left += 1
        return count
