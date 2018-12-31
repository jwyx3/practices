# https://leetcode.com/problems/koko-eating-bananas/
# https://leetcode.com/problems/koko-eating-bananas/solution/
#
# binary on answer
# similar to copy book

class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        
        def check(K):
            return sum((p - 1) / K + 1 for p in piles) <= H
        
        start, end = 1, max(piles)
        while start < end:
            mid = (start + end) / 2
            if check(mid):
                end = mid
            else:
                start = mid + 1
        return start
