class Solution:
    # @param s: a list of char
    # @param offset: an integer
    # @return: nothing

    # three steps rotations
    def rotateString(self, s, offset):
        if not s or offset < 0:
            return
        n = len(s)
        offset %= n
        self.reverse(s, 0, n - offset - 1)
        self.reverse(s, n - offset, n - 1)
        self.reverse(s, 0, n - 1)

    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
