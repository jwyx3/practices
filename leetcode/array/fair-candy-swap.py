# https://leetcode.com/problems/fair-candy-swap/
# https://leetcode.com/problems/fair-candy-swap/solution/

class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sA, sB = sum(A), sum(B)
        setB = set(B)
        for x in A:
            y = x + (sB - sA) / 2
            if y in setB:
                return [x, y]
