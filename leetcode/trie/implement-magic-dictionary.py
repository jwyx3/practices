class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word = False


class MagicDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def buildDict(self, words):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in words:
            node = self.root
            for c in word:
                node = node.children[c]
            node.word = True

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for new_word in self.next_word(word):
            node = self.root
            for c in new_word:
                node = node.children.get(c)
                if node is None:
                    break
            if node and node.word:
                return True
        return False

    def next_word(self, word):
        for i in xrange(len(word)):
            # 26 letters
            for c in "abcdefghijklmnopqrstuvwxyz":
                if word[i] != c:
                    yield word[:i] + c + word[i + 1:]
