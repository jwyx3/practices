class Solution:
    """
    @param A : an integer array
    @return : a integer
    """
    # XOR: exclusive or
    def singleNumber(self, A):
        ans = 0
        for x in A:
            ans ^= x
        return ans
