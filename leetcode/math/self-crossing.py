# https://leetcode.com/problems/self-crossing
# http://www.cnblogs.com/grandyang/p/5216856.html
# Time: O(N)
# Space: O(1)

class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        # three cases:
        # 1. line 1 meet 4
        # 2. line 1 meet 5
        # 3. line 1 meet 6
        for i in xrange(3, len(x)):
            if x[i] >= x[i-2] and x[i-3] >= x[i-1]:
                return True
            if i >= 4 and x[i-1] == x[i-3] and x[i-4] + x[i] >= x[i-2]:
                return True
            if i >= 5 and x[i-2] >= x[i-4] and x[i-3] >= x[i-1] and x[i-1] + x[i-5] >= x[i-3] and x[i-4] + x[i] >= x[i-2]:
                return True
        return False
