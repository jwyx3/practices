# https://leetcode.com/problems/numbers-at-most-n-given-digit-set/
# https://leetcode.com/problems/numbers-at-most-n-given-digit-set/solution/
# for dynamic programming solution, refer solution tab.
# Time: O(K*logM), M = len(D), K is digits of N.
# Space: O(K)

class Solution(object):
    def atMostNGivenDigitSet(self, D, N):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        """
        res = 0
        num = str(N)
        M, K = len(D), len(num)
        # for < K digits
        for k in xrange(1, K):
            res += M ** k
        # for K digits
        for i, x in enumerate(num):
            pos = bisect.bisect(D, str(x))
            if pos == 0:  # x < D[0], no valid numbers
                break
            # D[pos-1] <= x
            if D[pos-1] < str(x):
                res += pos * (M ** (K - i - 1))
                break
            else:
                res += (pos - 1) * (M ** (K - i - 1))
                # If it's last digit, need to handle D[pos-1] == str(x) case
                if i == K - 1:
                    res += 1
        return res

