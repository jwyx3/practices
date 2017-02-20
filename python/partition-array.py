class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        # you should partition the nums by k
        # and return the partition index as description
        if not nums or len(nums) == 0:
            return 0
        left, right = 0, len(nums) - 1
        while left <= right:
            # find first left element which >= k
            while left <= right and nums[left] < k:
                left += 1
            # find first right element which < k
            while left <= right and nums[right] >= k:
                right -= 1
            # if it's valid, swap
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return left
