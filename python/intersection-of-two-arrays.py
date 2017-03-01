class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))

class Solution1:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        d = dict.fromkeys(nums1, 1)
        ans = []
        for n in nums2:
            if d.get(n, 0) == 1:
                ans.append(n)
                d[n] += 1
        return ans
