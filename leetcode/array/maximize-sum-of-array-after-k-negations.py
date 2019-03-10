# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
# Time: O(NlogN)
# Space: O(1)
# 分类讨论，奇偶性

class Solution(object):
    def largestSumAfterKNegations(self, A, k):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        negs = 0
        sum_x, min_x = 0, float('inf')
        for x in A:
            if x < 0:
                if k > 0:
                    k -= 1
                    sum_x += abs(x)
                else:
                    negs += 1
                    sum_x += x
            else:
                sum_x += x
            min_x = min(min_x, abs(x))
        # if K > negs
        if negs == 0:
            # if K and negs are different (odd/even)
            if k & 1:
                return sum_x - 2 * min_x
        # If K <= negs or (K > negs and K and negs are odd or even)
        return sum_x
        
# improved sort
# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/discuss/252254/C%2B%2BPython-Sort

class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        negs, n, sum_x, min_x = 0, len(A), 0, float('inf')
        for i in xrange(n):
            if negs < K and A[i] < 0:
                A[i] = -A[i]
                negs += 1
            sum_x += A[i]
            min_x = min(min_x, abs(A[i]))
        # two cases:
        # K > total negatives, if K - negs is odd, flip back smallest abs
        # K <= total negatives, do nothing.
        return sum_x - (K - negs) % 2 * 2 * min_x
