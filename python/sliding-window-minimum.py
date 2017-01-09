from collections import deque

class Solution:
    """
    @param nums: A list of integers.
    @return: The minimum number inside the window at each moving.
    """
    # 单调非递减序列
    def mixSlidingWindow(self, nums, k):
        if not nums or k <= 0:
            return []
        q = deque()
        ans, n = [], len(nums)
        for i in xrange(n):
            while len(q) > 0 and q[-1] > nums[i]:
                q.pop()
            q.append(nums[i])

            if i >= k and q[0] == nums[i-k]:
                q.popleft()

            if i >= k - 1:
                ans.append(q[0])
        return ans

if __name__ == '__main__':
    s = Solution()
    print s.mixSlidingWindow([1, 2, 7, 7, 8], 3), "#", "[1, 2, 7]"
