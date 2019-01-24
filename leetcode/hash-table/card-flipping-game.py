# https://leetcode.com/problems/card-flipping-game/
# https://leetcode.com/problems/card-flipping-game/solution/
# Time: O(N)
# Space: O(N)
# if number appear at both front and back of same card, it can't candidate

class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        same = {a for a, b in itertools.izip(fronts, backs) if a == b}
        best = float('inf')
        for x in itertools.chain(fronts, backs):
            if x not in same:
                best = min(best, x)
        return best if best < float('inf') else 0
