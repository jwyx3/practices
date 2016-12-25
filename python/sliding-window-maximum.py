from collections import deque

class Solution:
    """
    @param nums: A list of integers.
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        if k == 0 or not nums:
            return []
        # 单调队列
        ans, d = [], deque()
        for i in xrange(len(nums)):
            # 比当前都小已经不可能成为最大数, 维护单调递减队列
            # d[-1] < nums[i] 处理重复情况
            while len(d) > 0 and d[-1] < nums[i]:
                d.pop()
            d.append(nums[i])

            # 如果移出窗口的数是最大数, 从队列中移出
            # 保证队列涵盖k个数
            if i >= k and nums[i - k] == d[0]:
                d.popleft()

            # 如何已经满足k长度的窗口, 开始记录最大数
            if i >= k - 1:
                ans.append(d[0])
        return ans
