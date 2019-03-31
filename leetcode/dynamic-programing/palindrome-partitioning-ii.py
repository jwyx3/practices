# https://leetcode.com/problems/palindrome-partitioning-ii/
# https://leetcode.com/problems/palindrome-partitioning-ii/discuss/42198/My-solution-does-not-need-a-table-for-palindrome-is-it-right-It-uses-only-O(n)-space.
# http://www.cnblogs.com/grandyang/p/4271456.html 
# Time: O(N**2)
# Space: O(N**2)

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # dp[i]: min cuts of s[:i+1]
        dp = range(n)
        # palindrome
        p = [[False] * n for _ in xrange(n)]
        for i in xrange(n):
            for j in xrange(i + 1):
                if s[j] == s[i] and (i - j < 2 or p[j+1][i-1]):
                    p[j][i] = True
                    dp[i] = min(dp[i], 0 if j == 0 else dp[j-1] + 1)
        return dp[n-1]

# better space
# Space: O(N)

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # dp[i]: min cuts of s[:i+1]
        dp = range(n)
        # palindrome
        p = [False] * n
        for i in xrange(n):
            np = [False] * n
            for j in xrange(i + 1):
                if s[j] == s[i] and (i - j < 2 or p[j+1]):
                    np[j] = True
                    dp[i] = min(dp[i], 0 if j == 0 else dp[j-1] + 1)
            p = np
        return dp[n-1]    
