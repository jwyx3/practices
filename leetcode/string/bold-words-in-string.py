# https://leetcode.com/problems/bold-words-in-string/
# https://leetcode.com/problems/bold-words-in-string/solution/

class Solution(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        mask = [0] * len(S)
        for i in xrange(len(S)):
            prefix = S[i:]
            for word in words:
                if prefix.startswith(word):
                    for j in xrange(i, min(i + len(word), len(S))):
                        mask[j] = 1
        res = []
        for i in xrange(len(S)):
            if mask[i] and (i == 0 or not mask[i - 1]):
                res.append('<b>')
            res.append(S[i])
            if mask[i] and (i == len(S) - 1 or not mask[i + 1]):
                res.append('</b>')
        return ''.join(res)
