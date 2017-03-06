class Solution:
    """
    @param nums: A list of integers.
    @return: An integer denotes the middle number of the array.
    """
    def median(self, nums):
        if not nums:
            return -1
        n = len(nums)
        # remember the k!!
        return self.kth(nums, 0, n - 1, n - n / 2)

    def kth(self, nums, start, end, k):
        if start == end:
            return nums[start]

        left, right = start, end
        mid = left + (right - left) / 2
        pivot, nums[mid] = nums[mid], nums[left]
        while left < right:
            # find last element < pivot
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left] = nums[right]
            # find first elemetn > pivot
            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]
        nums[left] = pivot

        if left == k - 1:
            return nums[left]
        elif left < k - 1:
            return self.kth(nums, left + 1, end, k)
        else:
            return self.kth(nums, start, left - 1, k)
