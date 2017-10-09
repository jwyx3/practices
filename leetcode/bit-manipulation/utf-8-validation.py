# credit: https://leetcode.com/problems/utf-8-validation/discuss/
class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        count = 0
        for i in data:
            # the begining of utf8 word
            if count == 0:
                if (i >> 5) == 0b110: count = 1
                elif (i >> 4) == 0b1110: count = 2
                elif (i >> 3) == 0b11110: count = 3
                elif i >> 7: return False
            else:
                if (i >> 6) != 0b10: return False
                count -= 1
        return count == 0
