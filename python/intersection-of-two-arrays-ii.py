from collections import Counter

class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        count = Counter(nums1)
        ans = []
        for n in nums2:
            if count[n] > 0:
                ans.append(n)
                count[n] -= 1
        return ans
