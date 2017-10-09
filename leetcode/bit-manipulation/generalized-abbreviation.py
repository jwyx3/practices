# idea: 1 => charactor, 0 => use number
class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        result = []
        n = 1 << len(word)
        for i in xrange(n):
            k, mask, abbr = 0, 1, []
            for j in xrange(len(word)):
                if i & mask:
                    if k > 0:
                        abbr.append(str(k))
                        k = 0
                    abbr.append(word[j])
                else:
                    k += 1
                mask <<= 1
            if k > 0:
                abbr.append(str(k))
            result.append(''.join(abbr))
        return result
