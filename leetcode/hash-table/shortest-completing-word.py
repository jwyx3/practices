# https://leetcode.com/problems/shortest-completing-word/
# https://leetcode.com/problems/shortest-completing-word/solution/

class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        def count(word):
            res = [0] * 26
            for c in word:
                res[ord(c) - ord('a')] += 1
            return res
        
        def cover(c0, c1):
            return all(x0 <= x1 for x0, x1 in itertools.izip(c0, c1))
        
        target = count([c.lower() for c in licensePlate if c.isalpha()])
        res = None
        for word in words:
            if (res is None or len(word) < len(res)) and cover(target, count(word)):
                res = word
        return res
