# idea: if even, halve it
#       if odd, xx11 except 3 -> +1; xx01 -> -1
#               create more tailing zeros

class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0: return 0
        result = 0
        while n > 1:
            if not n & 1:
                n >>= 1
            elif n & 0x2 and n != 3:
                n += 1
            else:
                n -= 1
            result += 1
        return result
