# https://leetcode.com/problems/goat-latin/
# Time: O(N)
# Space: O(N)

class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        ans = []
        for i, s in enumerate(S.split(), 1):
            if s[0] in 'aeiouAEIOU':
                ans.append(s + 'ma' + 'a' * i)
            else:
                ans.append(s[1:] + s[0] + 'ma' + 'a' * i)
        return ' '.join(ans)
            
