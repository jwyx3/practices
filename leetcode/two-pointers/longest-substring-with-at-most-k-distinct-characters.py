# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
# Time: O(N)
# Space: O(k), k is the number of unique charactors
# <unique char, number of char>

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # corner case
        if k <= 0 or not s:
            return 0
        # sliding window
        count = collections.Counter()
        unique = ans = j = 0
        for i, c in enumerate(s):
            count[c] += 1
            if count[c] == 1:
                unique += 1
                while j < i and unique > k:
                    count[s[j]] -= 1
                    if count[s[j]] == 0:
                        unique -= 1
                    j += 1
            ans = max(ans, i - j + 1)
        return ans

# different way of sliding window <unique char, rightmost position>
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/solution/

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # corner case
        if k <= 0 or not s:
            return 0
        # sliding window
        ans, j = 1, 0
        pos = collections.OrderedDict()
        for i, c in enumerate(s):
            if c in pos:
                del pos[c]
            pos[c] = i
            if len(pos) == k + 1:
                _, j = pos.popitem(last=False)  # j is removed element
                j += 1
            ans = max(ans, i - j + 1)
        return ans
