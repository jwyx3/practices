# https://leetcode.com/problems/maximum-length-of-repeated-subarray/
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/solution/
#
# Since a common subarray of A and B must start at some A[i] and B[j],
# let dp[i][j] be the longest common prefix of A[i:] and B[j:].
# Whenever A[i] == B[j], we know dp[i][j] = dp[i+1][j+1] + 1.
# Also, the answer is max(dp[i][j]) over all i, j.


class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # dp[i][j]: the longest common prefix of A[i:] and B[j:].
        # dp[i][j] = dp[i+1][j+1] + 1 if A[i] == B[j]; otherwise, 0
        # initial: dp[-1][*], dp[*][-1]
        # answer: max(dp[*][*])
        
        if not A or not B:
            return 0
        dp = [[0] * len(A) for _ in xrange(len(B))]
        for i in xrange(len(A)):
            if A[i] == B[-1]:
                dp[i][-1] = 1
        for j in xrange(len(B)):
            if B[j] == A[-1]:
                dp[-1][j] = 1
        for i in xrange(len(A) - 2, -1, -1):
            for j in xrange(len(B) - 2, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
        return max(max(dp[i]) for i in xrange(len(A)))
