class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        result = []
        for h in range(12):
            for m in range(60):
                # convert to binary and count 1
                if str(bin((h << 6) + m)).count('1') == num:
                    result.append("%s:%s" % (h, ('0' if m < 10 else '') + str(m)))
        return result
