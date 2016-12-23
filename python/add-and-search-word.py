class TrieNode(object):
    def __init__(self, is_word=False):
        self.is_word = is_word
        self.children = {}


class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        curr_node = self.root
        for letter in word:
            next_node = curr_node.children.get(letter, TrieNode())
            if letter not in curr_node.children:
                curr_node.children[letter] = next_node
            curr_node = next_node
        curr_node.is_word = True

    def _search(self, word, curr_node):
        if len(word) == 0:
            return curr_node.is_word

        letter = word[0]
        if letter == '.':
            for next_node in curr_node.children.values():
                if self._search(word[1:], next_node):
                    return True
        elif letter in curr_node.children:
            return self._search(word[1:], curr_node.children[letter])

        return False

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        return self._search(word, self.root)

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")

if __name__ == "__main__":
    wordDictionary = WordDictionary()
    wordDictionary.addWord("a")
    print wordDictionary.search(".")
