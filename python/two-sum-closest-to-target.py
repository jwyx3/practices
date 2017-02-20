import sys


class Solution:
    # @param {int[]} nums an integer array
    # @param {int} target an integer
    # @return {int} the difference between the sum and the target
    def twoSumClosest(self, nums, target):
        # Write your code here
        if not nums or len(nums) < 2:
            return None
        nums.sort()
        left, right = 0, len(nums) - 1
        ans = sys.maxint
        while left < right:
            nums_sum = nums[left] + nums[right]
            if abs(nums_sum - target) < ans:
                ans = abs(nums_sum - target)
            if nums_sum == target:
                return ans
            elif nums_sum > target:
                right -= 1
            else:
                left += 1
        return ans
