class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """
    # O(nlogn)
    def subarraySumClosest(self, nums):
        if not nums:
            return [-1, -1]
        sums = [0]
        for i in range(len(nums)):
            sums.append(sums[i] + nums[i])
        # sort
        sorted_sums = sorted([(s, i) for i, s in enumerate(sums)])
        min_diff, ans = sys.maxint, [-1, -1]
        for i in range(1, len(sorted_sums)):
            s1, i1 = sorted_sums[i - 1]
            s2, i2 = sorted_sums[i]
            if min_diff > abs(s1 - s2):
                min_diff = abs(s1 - s2)
                ans = [min(i1, i2), max(i1, i2) - 1]
        return ans

