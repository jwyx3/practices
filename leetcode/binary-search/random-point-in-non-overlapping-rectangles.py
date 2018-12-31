# https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/
#
# weighted random pick + binary search
# within bucket, calculate point coordicate
# Time: O(log(total points))
# Space: O(len(rects))

import random
import time

class Solution(object):
    
    def area(self, rect):
        return (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1)

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        if not rects or not rects[0]:
            return None
        self.rects = rects
        self.psums = []
        for rect in rects:
            area = self.area(rect)
            self.psums.append(area + (self.psums[-1] if self.psums else 0))
        #random.seed(time.time())

    def pick(self):
        """
        :rtype: List[int]
        """
        end = self.psums[-1] - 1
        target = random.randint(0, end) if end > 0 else 0
        start, end = 0, len(self.psums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if self.psums[mid] > target:
                end = mid
            else:
                start = mid + 1
        i = end
        if self.psums[start] > target:
            i = start
        base = self.psums[i] - self.area(self.rects[i])
        width = self.rects[i][2] - self.rects[i][0] + 1
        return [self.rects[i][0] + (target - base) % width, self.rects[i][1] + (target - base) / width]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
