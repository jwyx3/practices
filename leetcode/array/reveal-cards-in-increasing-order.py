# https://leetcode.com/problems/reveal-cards-in-increasing-order/
# https://leetcode.com/problems/reveal-cards-in-increasing-order/solution/
# simulation
# pick number in ascending order and simulate reveal order
# Time: O(NlogN), sort
# Space: O(N)

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        N = len(deck)
        indices = collections.deque(range(N))
        
        res = [0] * N
        for num in sorted(deck):
            res[indices.popleft()] = num
            if indices:
                indices.append(indices.popleft())
        return res
