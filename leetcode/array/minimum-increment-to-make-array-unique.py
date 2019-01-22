# https://leetcode.com/problems/minimum-increment-to-make-array-unique/
# Time: O(NlogN)
# Space: O(1)

class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res, t = 0, 0
        A.sort()
        for a in A:
            # calculate diff between target and current number
            res += max(0, t - a)
            t = max(t + 1, a + 1)
        return res
            
# Counting
# Time: O(K), K >= 40000 + 40000
# Space: O(K)
class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        count = collections.Counter(A)
        taken = []
        for i in xrange(100000):
            if count[i] >= 2:
                taken.extend([i] * (count[i] - 1))
            elif taken and count[i] == 0:
                res += i - taken.pop()
        return res
