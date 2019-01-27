# https://leetcode.com/problems/sentence-screen-fitting/
# https://leetcode.com/problems/sentence-screen-fitting/discuss/90845/21ms-18-lines-Java-solution
# http://www.cnblogs.com/grandyang/p/5975426.html
# use start to remember the start index of next row
# Time: O(R*C)
# Space: O(1)

class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        s = ' '.join(sentence) + ' '
        start = 0  # start index in repeated s for next row
        for r in xrange(rows):
            start += cols
            if s[start % len(s)] == ' ':
                start += 1 # next row should start with non-space
            else:
                while start > 0 and s[(start-1) % len(s)] != ' ':
                    start -= 1
        return start / len(s)
