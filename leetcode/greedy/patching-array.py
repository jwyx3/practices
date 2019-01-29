# https://leetcode.com/problems/patching-array/
# https://leetcode.com/problems/patching-array/solution/
# intuition: For any missing number, if we want to cover it, we have to add at least one number smaller or equal to that number. Otherwise, it will not be covered. Imagine you want to give someone change of xx cents, and you don't have enough coins. You will need to ask for coin less than or equal to xx.
# [1, miss) + [x, miss + x), x <= miss, so [1, miss+x) is covered
# min patching, so added x should be as large as possible if nums[i] > miss, then choose miss

class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        miss = 1
        res = i = 0
        while miss <= n:  # miss is exclusive, so use <=
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                res += 1
                miss += miss
        return res
