class Solution:
    # @param {int[]} nums an integer array
    # @param {int} target an integer
    # @return {int} the difference between the sum and the target
    def twoSumClosest(self, nums, target):
        if not nums or len(nums) < 2:
            return -1
        nums.sort()
        min_diff = sys.maxint
        left, right = 0, len(nums) - 1
        while left < right:
            diff = nums[left] + nums[right] - target
            if abs(diff) < min_diff:
                min_diff = abs(diff)
            if diff == 0:
                break
            elif diff > 0:
                right -= 1
            else:
                left += 1
        return min_diff
