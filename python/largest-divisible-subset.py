class Solution:
    # @param {int[]} nums a set of distinct positive integers
    # @return {int[]} the largest subset

    # dp[i]: the number of elements in the largest set which include A[i]
    # dp[i]: max{dp[j]} + 1 which A[i] % A[j] == 0 and j < i
    # initial: dp[i] = 1
    # answers: max[dp[i]]
    # use array prev to remember previous element
    # initial: prev[i] = i
    def largestDivisibleSubset(self, nums):
        # Write your code here
        if not nums:
            return []

        n = len(nums)
        dp = [1 for _ in range(n)]
        prev = [i for i in range(n)]

        nums.sort()
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j

        max_len, max_index = 0, 0
        for i in range(n):
            if dp[i] > max_len:
                max_len = dp[i]
                max_index = i

        ans, end = [], max_index
        while prev[end] != end:
            ans.insert(0, nums[end])
            end = prev[end]
        ans.insert(0, nums[end])
        return ans

