class Solution:
    """
    @param a, b: Two integer
    return: An integer
    """
    def bitSwapRequired(self, a, b):
        xor, ans = a ^ b, 0
        for i in range(32):
            if xor & 1:
                ans += 1
            xor >>= 1
        return ans
