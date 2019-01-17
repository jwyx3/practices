# https://leetcode.com/problems/max-chunks-to-make-sorted/
# https://leetcode.com/problems/max-chunks-to-make-sorted/solution/
# Time: O(N)
# Space: O(1)
# dp[i]: max chunks of first i elements
# dp[i] = dp[i-1] + max(nums[:i]) == i-1
# initial: dp[0] = 0
# answer: dp[len(nums)]

class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res, m = 0, -1
        for i, num in enumerate(arr):
            m = max(m, num)
            if i == m:
                res += 1
        return res
