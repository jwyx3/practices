# https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/
# https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/solution/
# Time: O(N)
# Space: O(N)

class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # swap[i]: make A and B increasing and swap A[i] and B[i]
        # noswap[i]: make A and B increasing and not swap A[i] and B[i]
        # if A[i-1] < A[i] and B[i-1] < B[i]:
        #   swap[i] = min(swap[i], swap[i-1] + 1)
        #   noswap[i] = min(noswap[i], noswap[i-1])
        # if A[i-1] < B[i] and B[i-1] < A[i]:
        #   swap[i] = min(swap[i], noswap[i-1] + 1)
        #   noswap[i] = min(noswap[i], swap[i-1])
        # initial: swap[0] = 1, noswap[0] = 0
        # answer: min(swap[N-1], noswap[N-1])
        # why two if: e.g. A = [1, 5, 4], B = [2, 3, 6]
        # make it short noswap: n, swap: s
        N = len(A)
        n1, s1 = 0, 1
        for i in xrange(1, N):
            n2 = s2 = float('inf')
            if A[i-1] < A[i] and B[i-1] < B[i]:
                s2 = min(s2, s1 + 1)
                n2 = min(n2, n1)
            if A[i-1] < B[i] and B[i-1] < A[i]:
                s2 = min(s2, n1 + 1)
                n2 = min(n2, s1)
            n1, s1 = n2, s2
        return min(n1, s1)
