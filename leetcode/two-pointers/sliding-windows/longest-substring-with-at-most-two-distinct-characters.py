# sliding window
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        result = j = 0
        count = collections.defaultdict(int)
        distinct = 0
        for i, c in enumerate(s):
            # process i
            count[c] += 1
            if count[c] == 1:
                distinct += 1
            # process j
            while distinct > 2:
                count[s[j]] -= 1
                if count[s[j]] == 0:
                    distinct -= 1
                j += 1
            # process result
            result = max(result, i - j + 1)
        return result
