class Solution:
    # @param {string} s A string
    # @return {int} the length of last word
    def lengthOfLastWord(self, s):
        length = 0
        for i in range(len(s) - 1, -1, -1):
            if length == 0:
                if s[i] == ' ':
                    continue
                length += 1
            else:
                if s[i] == ' ':
                    break
                length += 1
        return length
