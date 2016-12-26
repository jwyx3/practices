class Solution:
    # @param nums: a list of integers
    # @param s: an integer
    # @return: an integer representing the minimum size of subarray

    # 前缀和, O(n)
    def minimumSize(self, nums, s):
        if len(nums) == 0:
            return -1
        sums = [0]
        for i in xrange(len(nums)):
            sums.append(sums[i] + nums[i])
        ans, j = -1, 0
        for i in xrange(len(sums)):
            while j < len(sums) and sums[j] - sums[i] < s:
                j += 1
            if j < len(sums):
                if ans == -1 or j - i < ans:
                    ans = j - i
        return ans

    # O(nlogn) ?

