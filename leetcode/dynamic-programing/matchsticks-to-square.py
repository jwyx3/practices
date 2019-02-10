# https://leetcode.com/problems/matchsticks-to-square/
# https://leetcode.com/problems/matchsticks-to-square/solution/
# Time: O(N * 2**N), 2**N is total unique used bits, each step will check whole array
# Space: O(N + 2**N), call stack and used
# dynamic programming
# In any dynamic programming problem, what's important is that our problem must be breakable into smaller subproblems and also, these subproblems show some sort of overlap which we can save upon by caching or memoization.

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
        
        N = len(nums)
        memo = {}
        
        def dp(used, side_done):
            total = 0
            for i in xrange(N-1, -1, -1):
                if not (used & (1 << i)):
                    total += nums[N-1-i]
            if total > 0 and total % target == 0:
                side_done += 1
            if side_done == 3:
                return True
            if (used, side_done) in memo:
                return memo[used, side_done]
            res = False
            # remaining of current side
            rem = target * (int(total / target) + 1) - total
            for i in xrange(N-1, -1, -1):
                if nums[N-1-i] <= rem and (used & (1 << i)):
                    used &= ~(1 << i)
                    if dp(used, side_done):
                        res = True
                        break
                    used |= (1 << i)
            memo[used, side_done] = res
            return res
        
        return dp((1 << N) - 1, 0)
        
