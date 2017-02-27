class Solution:
    # @param heights: a list of integers
    # @return: an integer
    # 对撞指针
    def maxArea(self, heights):
        if not heights or len(heights) < 2:
            return 0
        left, right = 0, len(heights) - 1
        ans = 0
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            if area > ans:
                ans = area
            # always discard smaller boundary first
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return ans


