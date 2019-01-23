# https://leetcode.com/problems/find-and-replace-pattern/
# https://leetcode.com/problems/find-and-replace-pattern/solution/
# Time: O(N*K), K is length of words
# Space: O(N*K)

class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def match(word):
            m = {}
            for c1, c2 in zip(pattern, word):
                # be familiar with setdefault
                if m.setdefault(c1, c2) != c2:
                    return False
            # different charactor in word share same pattern
            return len(set(m.values())) == len(m.values())
        
        return [word for word in words if match(word)]
