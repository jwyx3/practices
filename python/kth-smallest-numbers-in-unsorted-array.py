class Solution:
    # @param {int} k an integer
    # @param {int[]} nums an integer array
    # return {int} kth smallest element

    # O(nlogn): sort
    def kthSmallest1(self, k, nums):
        if not nums or len(nums) < k:
            return -1
        nums.sort()
        return nums[k - 1]

    # O(n): quick select
    def kthSmallest(self, k, nums):
        if not nums or len(nums) < k:
            return -1
        return self.quickselect(nums, 0, len(nums) - 1, k)

    def quickselect(self, nums, start, end, k):
        # partition
        left, right = start, end
        mid = left + (right - left) / 2
        pivot = nums[mid]
        nums[mid] = nums[left]
        while left < right:
            # find last element < pivot
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left] = nums[right]
            # find first element > pivot
            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]
        nums[left] = pivot

        # split
        if left + 1 == k:
            return nums[left]
        elif left + 1 > k:
            return self.quickselect(nums, start, left, k)
        else:
            return self.quickselect(nums, left + 1, end, k)

