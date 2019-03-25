# https://leetcode.com/problems/best-sightseeing-pair/
# Time: O(N)
# Space: O(1)

class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        curr = ans = 0
        for i, num in enumerate(A):
            ans = max(ans, num - i + curr)
            curr = max(curr, num + i)
        return ans
