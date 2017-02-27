class Solution:
    # @param s: a string
    # @return: an integer

    # time O(n)
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        dt = dict.fromkeys(s, 0)
        ans, j = 0, 0
        for i in range(len(s)):
            while j < len(s) and dt[s[j]] < 1:
                dt[s[j]] += 1
                j += 1
            ans = max(ans, j - i)
            dt[s[i]] -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print s.lengthOfLongestSubstring("aaaa")
