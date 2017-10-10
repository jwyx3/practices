class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        j = 0
        for i in xrange(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # use j to record the end of new array
            nums[j] = nums[i]
            j += 1
        return j
