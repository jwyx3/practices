# https://leetcode.com/problems/find-the-derangement-of-an-array/
# https://leetcode.com/problems/find-the-derangement-of-an-array/solution/
# get recursion formula -> find duplicate -> use dp
# Time: O(N)
# Space: O(N) or O(1)
# d(n): the number of derangements for n elements
# 1. swap 0 and i (i > 0), A[0] and A[i] are known. -> become smaller problem d(n-2)
# 2. put A[0] into A[i], but don't put A[i] into A[0].
#    A[i] can't put into 0, so have n-2 choice
#    A[j], j!=i, can't put into j, so have n-2 choice
#    -> become smaller problem d(n-1)
# i can be any element except for 0. n-1 choice
# d(n) = (n-1) * (d(n-1) + d(n-2))
# initial: d(0) = 1, d(1) = 0
# answer: d(n)

class Solution(object):
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in xrange(2, n + 1):
            dp[i] = ((i-1)*(dp[i-1] + dp[i-2])) % MOD
        return dp[n]
