class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    # i and j are index of string
    # dp[i+1][j+1]: is s3[:i+j+1] formed by the interleaving of s1[:i+1] and s2[:j+1]
    # initial: dp[0][0] = True
    #          dp[i+1][0] = s1[:i+1] == s3[:i+1]
    #          dp[0][j+1] = s2[:j+1] == s3[:j+1]
    # dp[i+1][j+1] = dp[i][j+1] && s1[i] == s3[i+j+1] || dp[i+1][j] && s2[j] == s3[i+j+1]
    # answer: dp[len(s1)][len(s2)]
    def isInterleave(self, s1, s2, s3):
        if s1 is None or s2 is None or s3 is None:
            return False
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True
        for i in range(len(s1)):
            dp[i + 1][0] = s1[:i + 1] == s3[:i + 1]
        for j in range(len(s2)):
            dp[0][j + 1] = s2[:j + 1] == s3[:j + 1]

        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s3[i + j + 1]:
                    dp[i + 1][j + 1] = dp[i + 1][j + 1] or dp[i][j + 1]
                if s2[j] == s3[i + j + 1]:
                    dp[i + 1][j + 1] = dp[i + 1][j + 1] or dp[i + 1][j]
        return dp[len(s1)][len(s2)]

