# https://leetcode.com/problems/largest-sum-of-averages/
# https://leetcode.com/problems/largest-sum-of-averages/solution/
# Time: O(N*N*K)
# Space: O(N)

class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        # dp[i]: the largest score of A[i:] partitioning into at most K
        # k=1..K
        # dp[i] = max(average(i, N), max{average(i, j) + dp[j], j > i}))
        # average(i, j) = float(P[j] - P[i]) / (j - i)
        # initial: dp[i] = average(i, N)
        # answer: dp[0]
        
        N = len(A)
        P = [0]
        for num in A:
            P.append(P[-1] + num)
        
        def average(i, j):
            return float(P[j] - P[i]) / (j - i)
        
        dp = [0] * N
        for i in xrange(N):
            dp[i] = average(i, N)
        
        for k in xrange(K - 1):
            for i in xrange(N):
                for j in xrange(i + 1, N):
                    dp[i] = max(dp[i], average(i, j) + dp[j])
        return dp[0]
