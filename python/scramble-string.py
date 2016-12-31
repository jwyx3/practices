class Solution:
    # @param {string} s1 A string
    # @param {string} s2 Another string
    # @return {boolean} whether s2 is a scrambled string of s1

    # dp[x1][x2][s]: whether s1[x1:x1+s] and s2[x2:x2+s] are scramble
    # dp[x1][x2][s] = ANY( (dp[x1][x2][k] and dp[x1+k][x2+k][s-k]) or\
    #       (dp[x1][x2+s-k][k] and dp[x1+k][x2][s-k])), 1 <= k < s
    # initial: dp[x1][x2][1] = True  # if s1[x1] == s2[x2]
    #                        = False # otherwise
    # ans: dp[0][0][n]
    def isScramble(self, s1, s2):
        if not s1 or not s2 or len(s1) != len(s2):
            return False
        if len(s1) == 1 and len(s2) == 1:
            return s1 == s2
        n = len(s1)
        dp = [[[(s == 1 and s1[x1] == s2[x2]) for s in xrange(n+1)]
                for x2 in xrange(n)] for x1 in xrange(n)]
        for s in xrange(2, n+1):
            for x1 in xrange(n-s+1):
                for x2 in xrange(n-s+1):
                    for k in xrange(1, s):
                        dp[x1][x2][s] = dp[x1][x2][s] or\
                                (dp[x1][x2][k] and dp[x1+k][x2+k][s-k]) or\
                                (dp[x1][x2+s-k][k] and dp[x1+k][x2][s-k])
        return dp[0][0][n]

if __name__ == '__main__':
    s = Solution()
    print s.isScramble('rgtae', 'great'), '#', True
