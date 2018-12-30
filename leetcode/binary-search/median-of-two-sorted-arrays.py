# https://leetcode.com/problems/median-of-two-sorted-arrays/
# https://www.youtube.com/watch?v=LPFhl65R7ww
# Time: O(log(min(n1, n2)))

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1, n2 = len(nums1), len(nums2)
        # median:
        # if n1 + n2 is even: part1 + part2 = n1 + n2 - part1 - part2
        # if n1 + n2 is odd: part1 + part2 = n1 + n2 - part1 - part2 + 1
        # ->
        # start = 0
        # end = n1
        # part1 = (start + end) / 2
        # part2 = (n1 + n2 + 1) / 2 - part1
        #
        # maxLeft1 <= minRight2
        # maxLeft2 <= minRight1
        # 
        # if n1 + n2 is even: avg(max(maxLeft1, maxLeft2), min(minRight1, minRight2))
        # if n1 + n2 is odd: max(maxLeft1, maxLeft2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        start, end = 0, n1
        while start <= end:
            part1 = (start + end) / 2
            part2 = (n1 + n2 + 1) / 2 - part1
            maxL1 = nums1[part1 - 1] if part1 > 0 else float('-inf')
            minR1 = nums1[part1] if part1 < n1 else float('inf')
            maxL2 = nums2[part2 - 1] if part2 > 0 else float('-inf')
            minR2 = nums2[part2] if part2 < n2 else float('inf')
            if maxL1 <= minR2 and maxL2 <= minR1:
                if (n1 + n2) % 2 == 0:
                    return (max(maxL1, maxL2) + min(minR1, minR2)) / 2.0
                return max(maxL1, maxL2)
            elif maxL1 > minR2:
                end = part1 - 1
            else:
                start = part1 + 1
        raise Exception('invalid input')
