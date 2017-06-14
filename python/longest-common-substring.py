class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.

    # O(n * m)
    # dp[i+1][j+1]: the length of LCS of A[:i+1] and B[:j+1], ends with A[i] and B[j]
    # initial: dp[0][j] = 0, dp[i][0] = 0
    # dp[i+1][j+1] = dp[i][j] + 1 if A[i] == B[j]
    #              = 0 otherwise
    # answer: max{dp[i][j]}
    def longestCommonSubstring(self, A, B):
        if not A or not B:
            return 0
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = 0
        ans = dp[0][0]
        for i in range(len(A)):
            for j in range(len(B)):
                ans = max(ans, dp[i + 1][j + 1])
        return ans

