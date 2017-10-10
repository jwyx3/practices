# 先处理最大高度较小的那一侧
# 不断更新最大高度
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        left_h = right_h = 0
        l, r = 0, len(height) - 1
        result = 0
        while l <= r:
            if left_h <= right_h:
                result += max(left_h - height[l], 0)
                left_h = max(left_h, height[l])
                l += 1
            else:
                result += max(right_h - height[r], 0)
                right_h = max(right_h, height[r])
                r -= 1
        return result

