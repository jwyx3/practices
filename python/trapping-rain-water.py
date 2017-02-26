class Elevation(object):
    def __init__(self, h):
        self.height = h
        self.count = 1


class Solution:
    # @param heights: a list of integers
    # @return: a integer
    def trapRainWater(self, heights):
        ans = 0
        if len(heights) == 0:
            return ans

        deque = [Elevation(heights[0])]
        for i in xrange(1, len(heights)):
            left_height = deque[0].height
            new_el = Elevation(heights[i])
            while len(deque) > 0:
                if deque[-1].height >= heights[i]:
                    break
                last = deque.pop()
                # 只处理已知的右边界高度
                ans += (last.count * (min(heights[i], left_height) - last.height))
                # 保留宽度，用于之后处理未知部分
                new_el.count += last.count
            deque.append(new_el)
        return ans

    # @param heights: a list of integers
    # @return: a integer
    # 单纯 单调栈实现
    def trapRainWater0(self, heights):
        deque = [Elevation(heights[0])]
        for i in xrange(1, len(heights)):
            new_el = Elevation(heights[i])
            while len(deque) > 0:
                if deque[-1].height >= heights[i]:
                    break
                deque.pop()
            deque.append(new_el)
        return ans

    # two pointers
    def trapRainWater(self, heights):
        if not heights or len(heights) <= 2:
            return 0
        left, right = 0, len(heights) - 1
        ans, left_h, right_h = 0, 0, 0
        while left < right:
            # the water of smaller boundary is determined
            # the water it hold is determined by the max water height
            # of related side
            if heights[left] < heights[right]:
                left_h = max(left_h, heights[left])
                ans += (left_h - heights[left])
                left += 1
            else:
                right_h = max(right_h, heights[right])
                ans += (right_h - heights[right])
                right -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print s.trapRainWater([0,1,0,1,2,1,0,1,3,2,1,2,1]), 6

