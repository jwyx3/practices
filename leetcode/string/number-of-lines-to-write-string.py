# https://leetcode.com/problems/number-of-lines-to-write-string/
# Time: O(N)
# Space: O(1)

class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        if not S:
            return [0, 0]
        lines, width = 1, 0
        for c in S:
            w = widths[ord(c) - ord('a')]
            width += w
            if width > 100:
                lines += 1
                width = w
        return [lines, width]
