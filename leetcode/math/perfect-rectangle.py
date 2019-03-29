# https://leetcode.com/problems/perfect-rectangle/
# https://leetcode.com/problems/perfect-rectangle/discuss/87181/Really-Easy-Understanding-Solution(O(n)-Java)
# Time: O(N)
# Space: O(N)

class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        area = 0
        xm1 = ym1 = float('inf')  # min x and y
        xm2 = ym2 = float('-inf')  # max x and y
        corners = set()
        for x1, y1, x2, y2 in rectangles:
            xm1 = min(xm1, x1)
            ym1 = min(ym1, y1)
            xm2 = max(xm2, x2)
            ym2 = max(ym2, y2)
            
            area += (x2 - x1) * (y2 - y1)
            # non-corner points have even duplicates
            for x, y in ((x1, y1), (x2, y2), (x1, y2), (x2, y1)):
                if (x, y) in corners:
                    corners.discard((x, y))
                else:
                    corners.add((x, y))
        # only corner points appear only once
        if len(corners) != 4 or any(
                (x, y) not in corners for x, y in ((xm1, ym1), (xm2, ym2), (xm1, ym2), (xm2, ym1))):
            return False
        # size of rectangles equal to area of corner points
        return area == (xm2 - xm1) * (ym2 - ym1)
        
