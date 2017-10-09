# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # binary search
        start, end = 1, n
        while start + 1 < end:
            mid = start + (end - start) / 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1
        # 目的是为了不断缩小问题范围，最后从end和start中选择答案
        # 那么在end和start赋值阶段选择尽量都是bad version
        if isBadVersion(start):
            return start
        return end
