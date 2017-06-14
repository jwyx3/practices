class Solution:
    # @param {string} s a string,  encoded message
    # @return {int} an integer, the number of ways decoding

    # dp[i+1]: the total number of ways to decode message s[:i+1], 0<=i<len(s)
    # initial: dp[0] = 1
    # dp[i+1] = 0
    # dp[i+1] += dp[i] if s[i] >=1 and <=9
    # dp[i+1] += dp[i - 1] if int(s[i-1:i+1] >=10 and <=26
    # answer: dp[len(s)]
    def numDecodings(self, s):
        if not s:
            return 0
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        for i in range(len(s)):
            if 1 <= int(s[i]) <= 9:
                dp[i + 1] += dp[i]
            if i >= 1 and 10 <= int(s[i - 1:i + 1]) <= 26:
                dp[i + 1] += dp[i - 1]
        return dp[len(s)]


if __name__ == '__main__':
    s = Solution()
    print s.numDecodings("2226252724242221201918171615141311108787876761721201211012111989898911918293"), 47923200
