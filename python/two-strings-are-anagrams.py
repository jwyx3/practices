class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """

    # hash or sorting
    # What is Anagram?
    # - Two strings are anagram if they can be the same after change the order of characters.
    # not rotate

    # time: O(n)
    # space: O(1)
    def anagram(self, s, t):
        if not s or not t:
            return False
        if len(s) != len(t):
            return False
        d = [0 for _ in range(128)]
        for c in s:
            d[ord(c)] += 1
        for c in t:
            if d[ord(c)] == 0:
                return False
            d[ord(c)] -= 1
        return True
