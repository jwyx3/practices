class Solution:
    # @param dictionary: a list of strings
    # @return: a list of strings
    def longestWords(self, dictionary):
        max_len, max_words = 0, []
        for word in dictionary:
            if len(word) > max_len:
                max_len = len(word)
                max_words = [word]
            elif len(word) == max_len:
                max_words.append(word)
        return max_words
