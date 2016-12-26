class Solution:
    # @param heights: a list of integers
    # @return: an integer
    # 对撞指针
    def maxArea(self, heights):
        if len(heights) <= 1:
            return 0
        i, j = 0, len(heights) - 1
        ans, lh, rh = 0, 0, 0
        while i < j:
            # only higher height may increase size while the size is decreasing
            if heights[i] > lh:
                lh = heights[i]
            if heights[j] > rh:
                rh = heights[j]
            # update ans
            size = (j - i) * min(lh, rh)
            if ans == 0 or size > ans:
                ans = size
            # move pointer with lower height first
            if lh < rh:
                i += 1
            else:
                j -= 1
        return ans
