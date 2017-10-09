# n, m: len(larger array), len(smaller array)
# sort smaller array: O(mlogm + nlogm)
# sort larger array: O(nlogn + mlogn)
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2: return []
        result = set()
        nums1.sort()
        for num in nums2:
            if self.binary_search(nums1, num):
                result.add(num)
        return list(result)

    def binary_search(self, nums, x):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == x:
                return True
            elif nums[mid] < x:
                start = mid + 1
            else:
                end = mid - 1
        return x in (nums[end], nums[start])
