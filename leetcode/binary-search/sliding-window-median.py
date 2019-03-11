# https://leetcode.com/problems/sliding-window-median/
# more methods:
# https://leetcode.com/problems/sliding-window-median/solution/
# https://zxi.mytechroad.com/blog/difficulty/hard/leetcode-480-sliding-window-median/
# Time: O(klogk + (n - k)*k)
# Space: O(k)
# use bisect

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        window = sorted(nums[:k])
        
        def median():
            return (window[(k - 1) / 2] + window[k / 2]) * 0.5
        
        n = len(nums)
        ans = [median()]
        for i in xrange(k, n):
            window.pop(bisect.bisect_left(window, nums[i - k]))
            bisect.insort(window, nums[i])
            ans.append(median())
        return ans
