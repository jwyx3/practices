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

# no duplicate
class Solution:
    # @param nums: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, nums):
        if not nums:
            return None
        start, end = 0, len(nums) - 1
        target = nums[-1]
        while start + 1 < end:
            mid = start + (end - start) / 2
            # find first postion <= last number
            if nums[mid] <= target:
                end = mid
            else:
                start = mid
        return min(nums[start], nums[end])
