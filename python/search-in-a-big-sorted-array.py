"""
Definition of ArrayReader:
class ArrayReader:
    def get(self, index):
        # this would return the number on the given index
        # return -1 if index is less than zero.
"""
class Solution:
    # @param {ArrayReader} reader: An instance of ArrayReader
    # @param {int} target an integer
    # @return {int} an integer
    def searchBigSortedArray(self, reader, target):
        left, right = 0, 1
        while reader.get(right) < target and reader.get(right) != 2147483647:
            right += right
        if reader.get(right) == 2147483647:
            right -= 1

        while left + 1 < right:
            mid = left + (right - left) / 2
            if reader.get(mid) >= target:
                right = mid
            else:
                left = mid + 1
        if reader.get(left) == target:
            return left
        if reader.get(right) == target:
            return right
        return -1

