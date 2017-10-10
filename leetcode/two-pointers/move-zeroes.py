class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # the relative order of the non-zero elements
        if not nums: return
        j = 0
        for i, _ in enumerate(nums):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        # follow-up: what if we don't care about relative order
        # two pointer: left and right
        # why this has less operations?
        # previous solution: [0,0,1,2,3] => [1,2,3,0,0] => number of non-zeros swaps and n scan
        # current solution:  [0,0,1,2,3] => [3,2,1,0,0] => two swaps and n scan
        l, r = 0, len(nums) - 1
        while l < r:
            while l < r and nums[l] != 0:
                l += 1
            while l < r and nums[r] == 0:
                r -= 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

