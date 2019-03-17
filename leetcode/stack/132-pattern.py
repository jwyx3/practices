# https://leetcode.com/problems/132-pattern/
# http://www.cnblogs.com/grandyang/p/6081984.html
# Time: O(N)
# Space: O(N)

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # third is 2 of 132
        # stack save all number > third
        n = len(nums)
        third, stack = float('-inf'), []
        for i in xrange(n - 1, -1, -1):
            # if 1 < 2
            if nums[i] < third:
                return True
            # stack has potential j
            while stack and stack[-1] < nums[i]:
                third = stack.pop()
            stack.append(nums[i])
        return False

# follow up?
# return number 
# return all tuples
