# https://leetcode.com/problems/minimum-window-subsequence/
# TODO: check solution!
# convert from question: whether T is subsequence of S.
# Time: O(N*M), N is len(S), M is len(T)
# Space: O(M)

class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        # N, M = len(S), len(T)
        # dp[i][j]: length of subsequence S[:i] and T[:j]
        # if S[i-1] == T[j-1] and dp[i-1][j-1] >= 0:
        #   dp[i][j] = 1 + dp[i-1][j-1]
        # elif S[i-1] != T[j-1] and dp[i-1][j] >= 0:
        #   dp[i][j] = 1 + dp[i-1][j]
        # initial: dp[i][0] = 0, otherwise -1
        # answer: min(dp[k][M]), dp[k][M] > 0
        N, M = len(S), len(T)
        dp = [[-1] * (M + 1) for _ in xrange(2)]
        for i in xrange(2):
            dp[i][0] = 0
        res = ""
        for i in xrange(1, N+1):
            for j in xrange(1, M+1):
                if S[i-1] == T[j-1] and dp[(i-1)%2][j-1] >= 0:
                    dp[i%2][j] = 1 + dp[(i-1)%2][j-1]
                elif S[i-1] != T[j-1] and dp[(i-1)%2][j] >= 0:
                    dp[i%2][j] = 1 + dp[(i-1)%2][j]
            l = dp[i%2][M]
            if l >= 0 and (not res or len(res) > l):
                res = S[i-l:i]
        return res
