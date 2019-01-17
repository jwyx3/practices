# https://leetcode.com/problems/beautiful-array/
# idea: move number in the middle to right partition
# Time: O(NlogN)
# Space: O(NlogN)

class Solution(object):
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        res = range(1, N+1)
        self.helper(res, 0, N - 1)
        return res

    def helper(self, res, start, end):
        if start >= end:
            return
        n = end - start + 1
        curr = res[start:end + 1]
        si = ei = start
        sj = ej = start + (n + 1) / 2
        for k in xrange(len(curr)):
            if k & 1:
                res[ej] = curr[k]
                ej += 1
            else:
                res[ei] = curr[k]
                ei += 1
        self.helper(res, si, ei - 1)
        self.helper(res, sj, ej - 1)

# another way: https://leetcode.com/problems/beautiful-array/solution/
