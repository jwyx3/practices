# https://leetcode.com/problems/unique-substrings-in-wraparound-string/
# https://leetcode.com/problems/unique-substrings-in-wraparound-string/discuss/95439/Concise-Java-solution-using-DP
# Time: O(N)
# Space: O(N)

class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        # "abcdbcd": overlap, only need to check the longest substring
        # all contiguous substring are substring of s
        # dp[c]: the longest contiguous substring ending as c - 'a' charactor
        # answer: sum(dp)
        count = [0] * 26
        max_len = 0
        for i, c in enumerate(p):
            if i > 0 and (ord(p[i]) - ord(p[i-1]) == 1 or ord(p[i-1]) - ord(p[i]) == 25):
                max_len += 1
            else:
                max_len = 1
            j = ord(c) - ord('a')
            count[j] = max(count[j], max_len)
        return sum(count)
