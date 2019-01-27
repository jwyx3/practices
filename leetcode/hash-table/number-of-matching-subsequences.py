# https://leetcode.com/problems/number-of-matching-subsequences/
# https://leetcode.com/problems/number-of-matching-subsequences/solution/
# Time: O(len(S) + sum{len(word)})
# Space: O(sum{len(word}))
# Next Letter Pointers

class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        processing = collections.defaultdict(list)
        for i, word in enumerate(words):
            processing[word[0]].append((i, 0))
        
        res = 0
        for c in S:
            size = len(processing[c])
            for i in xrange(size):
                wi, start = processing[c][i]
                word, start = words[wi], start + 1
                if start < len(word):
                    processing[word[start]].append((wi, start))
                else:
                    res += 1
            if size:
                processing[c] = processing[c][size:]
        return res
        
