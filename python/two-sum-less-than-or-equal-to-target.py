class Solution:
    # @param nums {int[]} an array of integer
    # @param target {int} an integer
    # @return {int} an integer
    def twoSum5(self, nums, target):
        if not nums or len(nums) < 2:
            return 0
        nums.sort()
        count, left, right = 0, 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] <= target:
                count += (right - left)
                left += 1
            else:
                right -= 1
        return count
