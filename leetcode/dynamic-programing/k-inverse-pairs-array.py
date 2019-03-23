# https://leetcode.com/problems/k-inverse-pairs-array/
# https://leetcode.com/problems/k-inverse-pairs-array/solution/
# http://www.cnblogs.com/grandyang/p/7111385.html
# Time: O(N*K)
# Space: O(K)

class Solution(object):
    def kInversePairs(self, n, K):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # dp(i, j): how many different arrys consist of numbers from 1, i,
        #           such that there are exactly j inverse pairs
        # dp(i+1, j) = sum{dp(i, k)}, max(0,j-i)<=k<=j
        # initial: dp(1, 0) = 1, otherwise 0
        # answer: dp(n, K)
        
        MOD = 10 ** 9 + 7
        dp = [[0] * (K + 1) for _ in xrange(2)]
        dp[1][0] = 1
        
        for i in xrange(1, n):
            i0, i1 = i%2, (i+1)%2
            dp[i1][0] = 1
            for j in xrange(1, K + 1):
                # use accumulated value
                dp[i1][j] = (dp[i1][j-1] + dp[i0][j] - (dp[i0][j-i-1] if j > i else 0)) % MOD
        return dp[n%2][K]

