class Solution:
    # @param {int[]} nums a mountain sequence which increase firstly and then decrease
    # @return {int} then mountain top
    def mountainSequence(self, nums):
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if mid == 0 or mid == len(nums) - 1 or\
                    nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return nums[mid]
            if nums[mid-1] < nums[mid] and nums[mid] < nums[mid+1]:
                left = mid
            else:
                right = mid
        return max(nums[left], nums[right])
