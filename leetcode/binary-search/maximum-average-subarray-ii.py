# https://leetcode.com/problems/maximum-average-subarray-ii/
# Time: O(NlogN)
# Space: O(1)
# Try new template

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
    
        # check whether we can find subarray which average >= avg
        def check(avg):
            psum = prev = min_psum = 0
            for i in xrange(k):
                psum += nums[i] - avg
            if psum >= 0:
                return True
            for i in xrange(k, len(nums)):
                psum += nums[i] - avg
                prev += nums[i-k] - avg
                min_psum = min(min_psum, prev)
                if psum >= min_psum:
                    return True
            return False

        E = 1e-5
        lo, hi = min(nums), max(nums)
        while abs(lo - hi) > E:
            mid = (lo + hi) / 2.0
            # find max avarage meeting the requirement
            # g(m): don't have such avarage
            if not check(mid):
                hi = mid
            else:
                lo = mid
        return lo
