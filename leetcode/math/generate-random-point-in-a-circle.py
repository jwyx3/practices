# https://leetcode.com/problems/generate-random-point-in-a-circle/
# https://leetcode.com/problems/generate-random-point-in-a-circle/solution/
# Time: O(1) avg, O(inf) worst
# Space: O(1)

import random

class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.rad = radius
        self.xc = x_center
        self.yc = y_center        

    def randPoint(self):
        """
        :rtype: List[float]
        """
        while True:
            x = self.xc + random.uniform(-1, 1) * self.rad
            y = self.yc + random.uniform(-1, 1) * self.rad
            if (x - self.xc) ** 2 + (y - self.yc) ** 2 <= self.rad ** 2:
                return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()

# better answer??
# https://leetcode.com/problems/generate-random-point-in-a-circle/solution/

