class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        if not s:
            return ""
        return ' '.join(reversed(s.strip().split()))

