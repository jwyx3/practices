# https://leetcode.com/problems/set-intersection-size-at-least-two/
# http://www.cnblogs.com/grandyang/p/8503476.html
# greedy: end time ascending, and choose small interval first
# Time: O(NlogN), sort
# Space: O(1)
# how to handle at least k??

class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda (s, e): (e, -s))
        ans, p1, p2 = 0, -1, -1
        for i, (s, e) in enumerate(intervals):
            if s > p1 and s <= p2:
                # add one point into set
                ans += 1
                p1, p2 = p2, e
            elif s > p2:
                ans += 2
                p1, p2 = e - 1, e
        return ans
