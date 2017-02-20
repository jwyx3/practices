class Solution:
    # @param nums {int[]} an array of integer
    # @param target {int} an integer
    # @return {int} an integer
    def twoSum5(self, nums, target):
        # Write your code here
        if not nums:
            return 0

        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        while left < right:
            if nums[left] + nums[right] <= target:
                count += (right - left)
                left += 1
            else:
                right -= 1
        return count
