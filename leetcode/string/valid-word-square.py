# https://leetcode.com/problems/valid-word-square/
# https://leetcode.com/problems/valid-word-square/discuss/91125/Java-AC-Solution-Easy-to-Understand
# Time: O(N**2)
# Space: O(1)

class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        if not words or not words[0]:
            return True
        n = len(words)
        for i in xrange(n):
            for j in xrange(len(words[i])):
                if j >= n or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
        return True
