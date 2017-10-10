# sliding windows: two pointers
# substring -> all characters are continuous
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        count = collections.defaultdict(int)
        result, j = 0, 0
        for i, c in enumerate(s):
            count[c] += 1
            while count[c] > 1:
                count[s[j]] -= 1
                j += 1
            result = max(result, i - j + 1)
        return result
