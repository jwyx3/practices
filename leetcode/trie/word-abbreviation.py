# https://leetcode.com/problems/word-abbreviation/
# https://leetcode.com/problems/word-abbreviation/solution/
# Time: O(C)
# Space: O(C)

class Solution(object):
    def wordsAbbreviation(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        groups = collections.defaultdict(list)
        for i, word in enumerate(words):
            groups[len(word), word[0], word[-1]].append((word, i))
        
        ans = [None] * len(words)
        Trie = lambda: collections.defaultdict(Trie)
        COUNT = False
        
        for group in groups.itervalues():
            trie = Trie()
            for word, _ in group:
                curr = trie
                for c in word:
                    curr[c][COUNT] = curr[c].get(COUNT, 0) + 1
                    curr = curr[c]
            
            for word, i in group:
                curr, matched = trie, len(word)
                for j, c in enumerate(word):
                    if curr[c][COUNT] == 1:
                        matched = j
                        break
                    curr = curr[c]
                # include one distinct charactor
                if len(word) - matched - 1 > 2:
                    ans[i] = word[:matched + 1] + str(len(word) - matched - 2) + word[-1]
                else:
                    ans[i] = word
        return ans
