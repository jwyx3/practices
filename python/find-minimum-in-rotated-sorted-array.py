class Solution:
    # @param nums: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, nums):
        # write your code here
        if not nums:
            return None
        left, right = 0, len(nums) - 1
        # keep finding the range where A[left] > A[right]
        while left + 1 < right:
            mid = left + (right - left) / 2
            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid
        return min(nums[left], nums[right])
