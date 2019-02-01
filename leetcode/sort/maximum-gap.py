# https://leetcode.com/problems/maximum-gap/
# Time: O(n)
# Space: O(n)

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        nums = [(num, num) for num in nums]
        radix = collections.defaultdict(list)
        for i in xrange(10):
            complete = True
            for idx, num in nums:
                quot, rem = divmod(idx, 10)
                radix[rem].append((quot, num))
                if quot:
                    complete = False
            nums = []
            for j in xrange(10):
                if radix[j]:
                    nums.extend(radix[j])
                radix.pop(j)
            if complete:
                break
        return max(nums[k+1][1] - nums[k][1] for k in xrange(n-1))

