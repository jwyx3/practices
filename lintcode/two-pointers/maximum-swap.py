# https://www.lintcode.com/problem/maximum-swap
# Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.
# e.g 2736 -> 2736, 9973 -> 9973
#
# Time: O(N)
# Space: O(N), int to array

class Solution:
    """
    @param num: a non-negative intege
    @return: the maximum valued number
    """
    def maximumSwap(self, num):
        nums = list(str(num))
        n = len(nums)
        max_num, max_i = -1, -1
        swaps = None
        for i in xrange(n - 1, -1, -1):
            if nums[i] > max_num:
                max_num = nums[i]
                max_i = i
            if nums[i] < max_num:
                swaps = [i, max_i]
        if swaps:
            i, j = swaps
            nums[i], nums[j] = nums[j], nums[i]
        return int(''.join(nums))
