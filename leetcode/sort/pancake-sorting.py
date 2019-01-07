# https://leetcode.com/problems/pancake-sorting/
# https://leetcode.com/problems/pancake-sorting/discuss/214213/JavaC%2B%2BPython-Straight-Forward
# Time: O(N**2)
# swap max to A[0], then swap to the A[n-1]
# n -= 1

class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        for n in xrange(len(A), 0, -1):
            i = A.index(n)
            res.extend([i + 1, n])
            A = A[:i:-1] + A[:i]
        return res
