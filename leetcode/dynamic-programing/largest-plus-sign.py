# https://leetcode.com/problems/largest-plus-sign/
# https://leetcode.com/problems/largest-plus-sign/solution/
# Time: O(N**2)
# Space: O(N**2)

class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        mines = {tuple(x) for x in mines}
        dp = [[float('inf')] * N for _ in xrange(N)]
        
        for r in xrange(N):
            count = 0
            for c in xrange(N):
                count = 0 if (r, c) in mines else count + 1
                dp[r][c] = min(dp[r][c], count)
            count = 0
            for c in xrange(N-1, -1, -1):
                count = 0 if (r, c) in mines else count + 1
                dp[r][c] = min(dp[r][c], count)
        
        for c in xrange(N):
            count = 0
            for r in xrange(N):
                count = 0 if (r, c) in mines else count + 1
                dp[r][c] = min(dp[r][c], count)
            count = 0
            for r in xrange(N-1, -1, -1):
                count = 0 if (r, c) in mines else count + 1
                dp[r][c] = min(dp[r][c], count)
        
        res = 0
        for r in xrange(N):
            for c in xrange(N):
                res = max(res, dp[r][c])
        return res
                
