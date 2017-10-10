class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.index = -1 # word is distinct
        self.words = [] # all words which word[:i] is palindrome and suffix is word[i:]


# TLE!
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        root = self.buildTrie(words)
        result = []
        # two cases: 1)ab match a, 2) a match ba
        # handle duplicate case in 2: a match a
        for i, word in enumerate(words):
            node = root
            for j in xrange(-1, len(word)):
                if j >= 0:
                    node = node.children.get(word[j])
                    if not node:
                        break
                # case 1
                if node.index >= 0 and i != node.index and j < len(word) - 1 and\
                        self.isPalindrome(word, j + 1):
                    result.append([i, node.index])
            # case 2
            if node: result.extend([i, w] for w in node.words if w != i)
        return result

    def buildTrie(self, words):
        root = TrieNode()
        for i, word in enumerate(words):
            node, rev = root, word[::-1]
            # j == -1, handle whole word
            for j in xrange(-1, len(rev)):
                if j >= 0:
                    node = node.children[rev[j]]
                if self.isPalindrome(rev, j + 1):
                    node.words.append(i)
            node.index = i
        return root

    def isPalindrome(self, word, l):
        r = len(word) - 1
        while l < r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        return True

