# https://leetcode.com/problems/swap-adjacent-in-lr-string/
# https://leetcode.com/problems/swap-adjacent-in-lr-string/solution/
# change from state1 to state2. keep invariant.
# 1) same number of L and R between start and end
# 2) R in start must be before R in end; L in start must be after L in end.
# Time: O(N)
# Space: O(1), use generator + two pointers

class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        for (i, x), (j, y) in itertools.izip_longest(
                ((i, x) for i, x in enumerate(start) if x != 'X'),
                ((j, y) for j, y in enumerate(end) if y != 'X'),
                fillvalue=(None, None)):
            if x != y or (x == 'L' and i < j) or (y == 'R' and i > j):
                return False
        return True
