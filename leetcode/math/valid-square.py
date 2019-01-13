# https://leetcode.com/problems/valid-square/
# https://leetcode.com/problems/valid-square/discuss/103426/Share-my-simple-Python-solution
# idea: calculate distance of any two nodes. It should form two sets based on distance.
# handle corner case: four nodes should be different. i.e. no dist should be 0

class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def calc_dist(x, y):
            return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2
        
        points = [p1, p2, p3, p4]
        dists = collections.Counter()
        for i in xrange(4):
            for j in xrange(i+1, 4):
                dists[calc_dist(points[i], points[j])] += 1
        return set(dists.values()) == {2, 4} and 0 not in dists
