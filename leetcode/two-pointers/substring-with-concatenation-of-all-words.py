# Time: O(nm), hash
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words: return []
        result = []
        to_find = collections.Counter(words)
        m, n = len(words), len(words[0])
        for i in xrange(len(s) - n * m + 1):
            found = collections.defaultdict(int)
            j = 0
            while j < m:
                word = s[i + j * n:i + (j + 1) * n]
                if word not in to_find:
                    break
                found[word] += 1
                if found[word] > to_find[word]:
                    break
                j += 1
            if j == m:
                result.append(i)
        return result

