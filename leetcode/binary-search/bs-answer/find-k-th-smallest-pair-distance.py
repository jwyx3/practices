# https://leetcode.com/problems/find-k-th-smallest-pair-distance/
# Time: O(NlogN + NlogV), V = max(nums) - min(nums)
# Space: O(1)

class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()

        def check(mid):
            n = len(nums)
            j = count = 0
            for i in xrange(n):
                while j < i and nums[i] - nums[j] > mid:
                    j += 1
                count += i - j
            return count
        
        lo, hi = 0, nums[-1] - nums[0] + 1
        while lo < hi:
            mid = (lo + hi) / 2
            # the number of pairs with distance <= mid is >= k
            if check(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo 
