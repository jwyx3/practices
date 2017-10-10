# idea: l and r two pointers
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r: # use <= because we want to get length of new array
            while l <= r and nums[l] != val:
                l += 1
            while l <= r and nums[r] == val:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        return l
