class Solution:
    # @param s: a string
    # @return: a boolean
    def isUnique(self, str):
        # ASCII printable characters (character code 32-127)
        d = [0 for _ in range(128)]
        for c in str:
            if d[ord(c)] == 0:
                d[ord(c)] = 1
            else:
                return False
        return True
