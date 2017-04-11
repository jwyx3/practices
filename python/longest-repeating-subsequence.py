# longest common subsequence
# LTE!!
class Solution:
    # @param {string} str a string
    # @return {int} the length of the longest repeating subsequence
    # Time: O(n^2)
    def longestRepeatingSubsequence(self, str):
        n = len(str)
        dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if str[i - 1] == str[j - 1] and i != j:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n][n]

    # dp[i]: the longest repeating subsequence in first "i" characters
    # Time: O(n)
    def longestRepeatingSubsequence1(self, str):
        pass

if __name__ == '__main__':
    s = Solution()
    print s.longestRepeatingSubsequence1('aab'), 1
    print s.longestRepeatingSubsequence1('aabb'), 2
    print s.longestRepeatingSubsequence1('ajhsfjhasjfhjsaiuiwruwyruahfsjsahfkjjklkiiuairawkkdsjfaskjriwauieajdcnjahjaaaaaaabbbbbbbbbaakjshiuawieuuuwiupopowpoeajfkjsakf'), 56
