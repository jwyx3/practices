class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # keep related order
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        # follow-up: what if we don't care about relative order
        # two pointer: left and right
        # why this has less operations?
        # previous solution: [0,0,1,2,3] => [1,2,3,0,0] => number of non-zeros swaps and n scan
        # current solution:  [0,0,1,2,3] => [3,2,1,0,0] => two swaps and n scan
        left, right = 0, len(nums) - 1
        while left < right:
            while left < right and nums[left]:
                left += 1
            while left < right and not nums[right]:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]

