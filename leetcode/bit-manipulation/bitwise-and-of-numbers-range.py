# idea: 如果m != n，必然存在一个奇数和偶数，那么末位 AND 为0
#       不断右移m 和 n，然后记录移动位数

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # corner case!!
        if m == 0:
            return 0
        zeros = 1
        while m != n:
            m >>= 1
            n >>= 1
            zeros <<= 1
        return m * zeros
