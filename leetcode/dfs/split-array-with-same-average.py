# https://leetcode.com/problems/split-array-with-same-average/
# http://www.cnblogs.com/grandyang/p/10285531.html
# Time: O(2**N), len(A) is [1, 30]
# Space: O(N): call stack

class Solution(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        s, n = sum(A), len(A)
        A.sort()
        
        # sum/n == sum1/k
        # sum1 = sum * k / n
        # k: current numbers of set
        # curr: current sum of set
        def dfs(k, start, curr):
            if k == 0:
                return curr == 0
            for i in xrange(start, n):
                if i > start and A[i] == A[i-1]:
                    continue
                if curr < 0:  # A[i] >= 0
                    return False
                if dfs(k - 1, i + 1, curr - A[i]):
                    return True
            return False
        
        for k in xrange(1, n / 2 + 1):
            if (s * k) % n == 0 and dfs(k, 0, s * k / n):
                return True
        return False
