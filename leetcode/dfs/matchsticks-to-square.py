# https://leetcode.com/problems/matchsticks-to-square/
# https://leetcode.com/problems/matchsticks-to-square/solution/
# Time: O(4**N)
# Space: O(N)

class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """ 
        if not nums:
            return False
        
        target, rem = divmod(sum(nums), 4)
        if rem:
            return False
        
        nums.sort(reverse=True)
        
        if nums[0] > target:
            return False
        
        sides = [0] * 4
        # what subset a particular element belongs to?
        def dfs(start):
            if start == len(nums):
                return all(v == target for v in sides)
            # try 4 sides for each matchstick
            for i in xrange(4):
                if sides[i] + nums[start] <= target:
                    sides[i] += nums[start]
                    if dfs(start + 1):
                        return True
                    sides[i] -= nums[start]
            return False
        
        return dfs(0)
        

# dynamic programming
# In any dynamic programming problem, what's important is that our problem must be breakable into smaller subproblems and also, these subproblems show some sort of overlap which we can save upon by caching or memoization.

