class Solution:
    # @param n, an integer
    # @return an integer

    # reverse bits
    def reverseBits(self, n):
        result, mask = 0, 1
        for i in xrange(32):
            result <<= 1
            if n & mask: result |= 1
            mask <<= 1
        return result

    # 优化多次访问
    # 翻转后的值
    cache = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]

    def reverseBits(self, n):
        result, mask = 0, 0xf
        for i in range(8):
            result <<= 4
            result |= self.cache[mask & n]
            n >>= 4
        return result
