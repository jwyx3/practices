class Solution:
    # @param s: a string
    # @return: an integer
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        dt = dict.fromkeys(s, 0)
        ans, j = 0, 0
        for i in xrange(len(s)):
            while j < len(s) and dt[s[j]] < 1:
                dt[s[j]] += 1
                j += 1
            length = j - i
            if length > ans:
                ans = length
            dt[s[i]] -= 1
            i += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print s.lengthOfLongestSubstring('z'), '#', '1'
    print s.lengthOfLongestSubstring('aaaa'), '#', '1'
