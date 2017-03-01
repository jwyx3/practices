import sys


class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    # maximum from two directions
    def maxTwoSubArrays(self, nums):
        if not nums or len(nums) < 2:
            return 0

        left = [0 for _ in range(len(nums))]
        ans, min_sum, s = -sys.maxint, 0, 0
        for i in range(len(nums)):
            s += nums[i]
            ans = max(ans, s - min_sum)
            min_sum = min(min_sum, s)
            left[i] = ans

        right = [0 for _ in range(len(nums))]
        ans, min_sum, s = -sys.maxint, 0, 0
        for i in range(len(nums) - 1, -1, -1):
            s += nums[i]
            ans = max(ans, s - min_sum)
            min_sum = min(min_sum, s)
            right[i] = ans

        ans = -sys.maxint
        for i in range(len(nums) - 1):
            ans = max(ans, left[i] + right[i + 1])
        return ans

if __name__ == '__main__':
    s = Solution()
    print s.maxTwoSubArrays([-1, -1])
