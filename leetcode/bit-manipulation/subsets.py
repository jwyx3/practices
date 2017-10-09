class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return []
        result = []
        self.helper(nums, 0, [], result)
        return result

    def helper(self, nums, start_index, subset, result):
        result.append(subset[:])
        for i in range(start_index, len(nums)):
            subset.append(nums[i])
            self.helper(nums, i + 1, subset, result)
            subset.pop()

    def subsets(self, nums):
        if not nums: return []
        n = 1 << len(nums)
        result = []
        for i in xrange(n):
            subset = []
            for j in xrange(len(nums)):
                if i & (1 << j):
                    subset.append(nums[j])
            result.append(subset)
        return result
