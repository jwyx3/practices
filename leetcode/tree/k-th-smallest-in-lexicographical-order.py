# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/
# http://www.cnblogs.com/grandyang/p/6031787.html
# Time: O(logN * logN), iterate logN levels and each level takes logN to get steps
# Space: O(1)

class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        #  n, k = 13, 2
        # 0
        # 1            2 3 4 5 6 7 8 9
        # 10 11 12 13
        # preorder traversal
        # go to subtree or next sibling
        # need to get the size of subtree
        ans = 1
        k -= 1
        # [lo, hi)
        while k > 0:
            steps, lo, hi = 0, ans, ans + 1
            while lo <= n:
                steps += min(n + 1, hi) - lo
                lo, hi = lo * 10, hi * 10
            if steps <= k:
                k -= steps
                ans += 1
            else:
                k -= 1
                ans *= 10
        return ans
