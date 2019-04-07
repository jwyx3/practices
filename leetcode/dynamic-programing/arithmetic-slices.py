# https://leetcode.com/problems/arithmetic-slices/
# Time: O(n)
# Space: O(1)

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # dp[i]: the number of arithmetic slices ending with A[i], 0<=i<len(A)
        # dp[i] = dp[i-1] + 1 if A[i]-A[i-1] == A[i-1]-A[i-2]
        #       = 0           otherwise
        # for 2<=i<len(A)
        # initial: dp[0,1] = 0
        # answer: sum(dp)
        #
        #if not A: return 0
        #dp = [0] * len(A)
        #for i in xrange(2, len(A)):
        #    if A[i] - A[i-1] == A[i-1] - A[i-2]:
        #        dp[i] = dp[i-1] + 1
        #    else:
        #        dp[i] = 0
        #return sum(dp)
    
        # rolling array, time: O(n), space: O(1)
        if not A: return 0
        dp, ans = 0, 0
        for i in xrange(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp = dp + 1
            else:
                dp = 0
            ans += dp
        return ans
