class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        ans, stack = 0, []
        height.append(-1)
        # get all max area with height[i]
        for i in range(len(height)):
            while stack and height[i] <= height[stack[-1]]:
                h, w = height[stack.pop()], i
                if stack:
                    w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        return ans
