# https://leetcode.com/problems/strange-printer/
# similar: https://leetcode.com/problems/remove-boxes/
# Time: O(n**3)
# Space: O(n**2)

class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp(i, j): min number of turns to print A[i:j+1]
        # dp(i, j) = min(dp(i+1, m-1) + dp(m, j)), m > i and A[m] == A[i]
        # initial: dp(i, i-1) = 0, dp(i, i) = 1
        # answer: dp(0, n-1)
        n = len(s)
        memo = {}
        
        def dp(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if (i, j) in memo:
                return memo[i, j]
            while i < j and s[i] == s[i+1]:
                i += 1
            best = 1 + dp(i+1, j)
            for m in xrange(i+1, j+1):
                if s[m] == s[i]:
                    best = min(best, dp(i+1, m-1) + dp(m, j))
            memo[i, j] = best
            return best
        
        return dp(0, n-1)
