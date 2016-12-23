class Solution:
    # @param S: a list of integers
    # @return: a integer
    def triangleCount(self, S):
        # corner cases:
        # 1. len(s) < 3
        count = 0
        if len(S) < 3:
            return count
        # sort
        S = sorted(S)
        # pick one
        for z in xrange(2, len(S)):
            x, y = 0, z - 1
            while x < y:
                if S[x] + S[y] > S[z]:
                    count += (y - x)
                    y -= 1
                else:
                    x += 1
        return count
