class Solution:
    # @param nums {int[]} a list of integers
    # @param k {int} size of window
    # @return {int[]} the sum of element inside the window at each moving
    def winSum(self, nums, k):
        if nums is None or k <= 0 or len(nums) < k:
            return []
        ans, total = [], 0
        for i, num in enumerate(nums):
            total += num
            if i >= k:
                total -= nums[i - k]
            if i >= k - 1:
                ans.append(total)
        return ans
