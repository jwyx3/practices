# https://leetcode.com/problems/reverse-pairs/
# https://leetcode.com/problems/reverse-pairs/solution/
# TODO: check more solutions!!
# Time: O(N**2)
# Space: O(N)

class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ans, visited = 0, []
        for num in nums:
            i = bisect.bisect(visited, 2 * num)
            ans += len(visited) - i
            bisect.insort(visited, num)
        return ans
