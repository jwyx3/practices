class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))

    def intersection(self, nums1, nums2):
        nums_dict = dict.fromkeys(nums1, 1)
        ans = []
        for n in nums2:
            if nums_dict.get(n, 0) == 1:
                nums_dict[n] += 1
                ans.append(n)
        return ans

