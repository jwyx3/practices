#class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests failed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a
# bad version.
class Solution:
    """
    @param n: An integers.
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        if n <= 0:
            return -1
        left, right = 1, n
        while left + 1 < right:
            mid = left + (right - left) / 2
            if not SVNRepo.isBadVersion(mid):
                left = mid + 1
            else:
                right = mid
        if SVNRepo.isBadVersion(left):
            return left
        if left != right and SVNRepo.isBadVersion(right):
            return right
        return -1

#class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a
# bad version.
class Solution:
    """
    @param n: An integers.
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        if n <= 0:
            return -1
        start, end = 1, n
        while start + 1 < end:
            mid = start + (end - start) / 2
            if SVNRepo.isBadVersion(mid):
                end = mid
            else:
                start = mid
        if SVNRepo.isBadVersion(start):
            return start
        elif SVNRepo.isBadVersion(end):
            return end
        return -1
