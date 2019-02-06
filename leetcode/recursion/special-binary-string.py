# https://leetcode.com/problems/special-binary-string/
# https://leetcode.com/problems/special-binary-string/solution/
# Time: O(N**2)
# Space: O(N)

class Solution(object):
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        # swap special substring
        # similar to valid parenthese
        if not S:
            return ''
        res = []
        i = count = 0
        for j, c in enumerate(S):
            count += 1 if c == '1' else -1
            if count == 0:
                res.append('1' + self.makeLargestSpecial(S[i+1:j]) + '0')
                i = j + 1
        return ''.join(sorted(res, reverse=True))
