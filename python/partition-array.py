class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    # O(n)
    def partitionArray(self, nums, k):
        if not nums:
            return 0
        left, right = 0, len(nums) - 1
        while left <= right:
            # find first >=k
            while left <= right and nums[left] < k:
                left += 1
            # find last < k
            while left <= right and nums[right] >= k:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return left

