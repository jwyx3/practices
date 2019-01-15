# https://leetcode.com/problems/reordered-power-of-2/
# https://leetcode.com/problems/reordered-power-of-2/solution/
# because N <= 1e9, so it can only be 2**0, 2**1, ..., 2**29

class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        count = collections.Counter(str(N))
        return any(count == collections.Counter(str(1 << b)) for b in xrange(30))
