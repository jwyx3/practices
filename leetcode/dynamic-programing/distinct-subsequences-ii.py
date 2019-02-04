# https://leetcode.com/problems/distinct-subsequences-ii/
# https://leetcode.com/problems/distinct-subsequences-ii/solution/
# Time: O(N)
# Space: O(N)

# dp[i]: the number of distinct subsequences that use letters S[0], S[1], ..., S[i-1]
# last[S[i]]: index of last S[i]
# dp[i] = 2*dp[i-1] - dp[last[S[i]]-1]
# initial: dp[0] = 1, {''}
# answer: dp[N]-1, non-empty

class Solution(object):
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        n = len(S)
        # dp[0] = 1 because of empty string
        dp =  [1] + [0] * n
        last = {}
        for i in xrange(1, n + 1):
            c = S[i-1]
            dp[i] = 2 * dp[i-1]
            if c in last:
                dp[i] -= dp[last[c] - 1]
            last[c] = i
        return (dp[n] - 1) % (10 ** 9 + 7)  # remove empty
        
