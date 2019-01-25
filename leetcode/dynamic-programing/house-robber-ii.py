# https://leetcode.com/problems/house-robber-ii/
# Since House[1] and House[n] are adjacent, they cannot be robbed together. Therefore, the problem becomes to rob either House[1]-House[n-1] or House[2]-House[n], depending on which choice offers more money. Now the problem has degenerated to the House Robber, which is already been solved.
# Time: O(N)
# Space: O(1)

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        N = len(nums)
        if N == 1:
            return nums[0]

        dp0 = [0, nums[0]]
        for i in xrange(2, N):
            dp0[i%2] = max(dp0[(i-2)%2] + nums[i-1], dp0[(i-1)%2])
        
        dp1 = [0, nums[1]]
        for i in xrange(2, N):
            dp1[i%2] = max(dp1[(i-2)%2] + nums[i], dp1[(i-1)%2])
        
        return max(dp0[(N-1)%2], dp1[(N-1)%2])
