class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        s = '0123456789abcdef'
        result = ''.join(s[num >> (4 * i) & 0xf] for i in xrange(8)).rstrip('0')
        return '0' if not result else result[::-1]
