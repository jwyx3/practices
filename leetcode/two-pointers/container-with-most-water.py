# two pointers: if height[l] < height[r], l += 1; otherwise, r -= 1

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        l, r = 0, len(height) - 1
        result = 0
        while l < r:
            # the width is r - l instead of r - l + 1
            result = max(result, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return result
