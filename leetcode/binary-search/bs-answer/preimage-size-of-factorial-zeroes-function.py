# https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/
# https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/solution/
# Time: O(log5(10*K)*log2(10*K))
# Space: O(1)

class Solution(object):
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        # 2 * 5 = 10. count(2) > count(5)
        # so f(x) = K. -> f(x) = x/5 + x/(5**2) + x/(5**3) + ... = K
        # assume x0 is the smallest number f(x0) = K
        # then 5 numbers which belongs to [x0, x0+4] are valid. -> count is 5
        # otherwise, 0
        # find x which f(x) = K. return 5 if found, otherwise, return 0
        def check(x):
            count, d = 0, 5
            while x >= d:
                count += x / d
                x /= d
            return count
        
        lo, hi = 0, 10*K + 1
        while lo < hi:
            mid = (lo + hi) / 2
            count = check(mid)
            if count == K:
                return 5
            elif count > K:
                hi = mid
            else:
                lo = mid + 1
        return 0
