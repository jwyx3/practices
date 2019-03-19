# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/
# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/solution/
# Time: O(N)
# Space: O(N)

class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, K):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # n = len(nums)
        # w[i]: sum(nums[i:i+K])
        # left[i]: index of max w[m] for m=[0, i]
        # right[i]: index of max w[m] for m=[i,n-K]
        # find such j that argmax{w[j] + w[left[j-K]] + w[right[j+K]]}
        n = len(nums)
        w = [0] * (n - K + 1)
        for i, num in enumerate(nums):
            if i < K:
                w[0] += num
            else:
                w[i-K+1] = w[i-K] + num - nums[i-K]
        
        left, right = range(n), range(n)
        for i in xrange(1, n - 3 * K + 1):
            if w[left[i]] <= w[left[i - 1]]:
                left[i] = left[i - 1]
        
        for k in xrange(n - K - 1, 2 * K - 1, -1):
            if w[right[k]] <= w[right[k + 1]]:
                right[k] = right[k + 1]
        
        best, ans = 0, -1
        for j in xrange(K, n - 2 * K + 1):
            s = w[left[j-K]] + w[j] + w[right[j+K]]
            if s > best:
                best, ans = s, j
        return [left[ans - K], ans, right[ans + K]]
    
