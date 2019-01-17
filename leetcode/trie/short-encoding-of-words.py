# https://leetcode.com/problems/short-encoding-of-words/
# https://leetcode.com/problems/short-encoding-of-words/solution/
# Time: O(sum of length of words)
# Space: O(sum of length of words)

Trie = lambda: collections.defaultdict(Trie)


class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # de-dup
        words = list(set(words))
        trie = Trie()
        # all nodes with word
        nodes = [reduce(dict.__getitem__, word[::-1], trie) for word in words]
        # return sum of all leaves
        return sum(len(word) + 1 for i, word in enumerate(words) if not nodes[i])
