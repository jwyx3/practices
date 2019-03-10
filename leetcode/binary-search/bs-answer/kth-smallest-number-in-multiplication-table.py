# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/
# https://zxi.mytechroad.com/blog/algorithms/binary-search/leetcode-668-kth-smallest-number-in-multiplication-table/
# Time: O(Mlog(M*N))
# Space: O(1)

class Solution(object):
    def findKthNumber(self, m, n, K):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        # return number of number <= mid
        def check(mid):
            count = 0
            for r in xrange(m):
                # 1*(r+1), 2*(r+1), ..., n*(r+1) <= mid
                count += min(n, mid / (r + 1))
            return count
        
        lo, hi = 1, m * n + 1
        while lo < hi:
            mid = (lo + hi) / 2
            if check(mid) >= K:
                hi = mid
            else:
                lo = mid + 1
        return lo
