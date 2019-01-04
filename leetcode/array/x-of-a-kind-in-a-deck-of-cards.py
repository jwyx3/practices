# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/solution/

class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        from fractions import gcd
        return reduce(gcd, collections.Counter(deck).itervalues()) >= 2
