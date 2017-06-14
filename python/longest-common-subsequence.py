class Solution:
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """
    # dp[i+1][j+1]: LCS of A[:i+1] and B[:j+1], 0<=i<len(A), 0<=j<len(B)
    # initial: dp[i][0] = 0, dp[0][j] = 0
    # dp[i+1][j+1] = dp[i][j] + 1 if A[i] == B[j]
    #              = max(dp[i+1][j], dp[i][j+1]) if A[i] != B[j]
    # answer: dp[i+1][j+1]
    def longestCommonSubsequence(self, A, B):
        if not A or not B:
            return 0
        dp = [[False] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) + 1):
            dp[i][0] = 0
        for j in range(len(B) + 1):
            dp[0][j] = 0
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[len(A)][len(B)]
