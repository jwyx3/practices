# https://leetcode.com/problems/count-of-range-sum/
# https://leetcode.com/problems/count-of-range-sum/discuss/77990/Share-my-solution
# Time: O(NlogN)
# Space: O(N)

class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        # lower <= psums[j] - psums[i] <= upper
        # psums[i] + lower <= psums[j] <= psums[i] + upper
        # ->
        # psums[i] + lower <= psums[j1], first j1
        # psums[i] + upper < psums[j2], first j2
        # count = j2 - j1
        N = len(nums)
        psums = [0] * (N + 1)
        for i, num in enumerate(nums):
            psums[i + 1] = psums[i] + num

        # return count of range meeting such sum
        def mergesort(psums, start, end):
            if start + 1 >= end:
                return 0
            mid = (start + end) / 2
            ans = mergesort(psums, start, mid) + mergesort(psums, mid, end)
            psums1 = [0] * (end - start)
            i1 = 0
            j1 = j2 = j3 = mid
            for i in xrange(start, mid):
                while j1 < end and psums[j1] - lower < psums[i]:
                    j1 += 1
                while j2 < end and psums[j2] - upper <= psums[i]:
                    j2 += 1
                while j3 < end and psums[j3] < psums[i]:
                    psums1[i1] = psums[j3]
                    i1 += 1
                    j3 += 1
                ans += j2 - j1
                psums1[i1] = psums[i]
                i1 += 1
            psums[start:j3] = psums1[:i1]
            return ans

        return mergesort(psums, 0, N + 1)
