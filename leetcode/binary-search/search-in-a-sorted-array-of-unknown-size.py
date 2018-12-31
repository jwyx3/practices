# https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/
#
# identify the end of binary search

class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        NOT_EXIST = 2147483647
        start, end = 0, 1
        while reader.get(end) != NOT_EXIST:
            end *= 2
        while start + 1 < end:
            mid = start + (end - start) / 2
            val = reader.get(mid)
            if val == target:
                return mid
            elif val == NOT_EXIST or val > target:
                end = mid - 1
            else:
                start = mid + 1
        for i in (start, end):
            if reader.get(i) == target:
                return i
        return -1
