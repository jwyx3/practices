# https://leetcode.com/problems/escape-the-ghosts/
# Time: O(N)
# Space: O(1)

class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        # to avoid meeting at target, dist(you, target) < dist(ghost, target)
        # to avoid meeting at point k (!= target), dist(you, k) < dist(ghost, k)
        # => dist(you, k) + dist(k, target) < dist(ghost, k) + dist(k, target)
        # => dist(you, target) < dist(ghost, target)
        # so for all ghost, dist(you, target) < min{dist(ghost, target)}
        t0, t1 = target
        dist = abs(t0) + abs(t1)
        for g in ghosts:
            if abs(g[0] - t0) + abs(g[1] - t1) <= dist:
                return False
        return True

