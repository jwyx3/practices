# https://leetcode.com/problems/delete-columns-to-make-sorted-iii/
# https://leetcode.com/problems/delete-columns-to-make-sorted-iii/solution/
# Time: O(N*M*M), N = len(A), M = len(A[0])
# Space: O(M)
# calculate elements to keep instead of delete

class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        # convert ot LIS
        # N = len(A), M = len(A[0])
        # dp(i): the largest length of array if we keep index i. i=0..M-1
        # dp(i) = max{dp(j) + 1}, j<i, A[k][j] <= A[k][i], k=0..N-1
        # initial: dp(i) = 1
        # answer:  M - max(dp)
        
        N, M = len(A), len(A[0])
        dp = [1] * M
        for i in xrange(1, M):
            for j in xrange(i):
                if all(A[k][j] <= A[k][i] for k in xrange(N)):
                    dp[i] = max(dp[i], dp[j] + 1)
        return M - max(dp)
