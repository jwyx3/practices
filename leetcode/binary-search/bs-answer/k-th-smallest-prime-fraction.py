# https://leetcode.com/problems/k-th-smallest-prime-fraction/
# http://www.cnblogs.com/grandyang/p/10285531.html
# Time: O(Nlog(W)), W = (1 - 0) / 1e-9 = 1e9
# Space: O(1)

class Solution(object):
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        # return count of fraction <= x and the largest fraction
        def check(mid):
            n, j, k = len(A), 0, 0
            p, q = 0, 1
            for i in xrange(n):
                while j < n and A[i] > mid * A[j]:
                    j += 1
                k += n - j
                if j < n and p * A[j] < q * A[i]:
                    p, q = A[i], A[j]
            return k, (p, q)        
        
        E = 1e-9
        lo, hi = 0, 1
        while hi - lo > 1e-9:
            mid = (lo + hi) / 2.0
            k, (p, q) = check(mid)
            if k == K:
                return [p, q]
            elif k < K:
                lo = mid
            else:
                hi = mid
        return [-1, -1]
