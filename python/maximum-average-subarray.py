from collections import deque

class Solution:
    # @param {int[]} nums an array with positive and negative numbers
    # @param {int} k an integer
    # @return {double} the maximum average
    def maxAverage(self, nums, k):
        def check(x):
            n, min_sums = len(nums), 0
            ans, sums = False, [0]
            for i in xrange(1, n+1):
                sums.append(sums[i-1] + nums[i-1] - x)
                if i >= k:
                    min_sums = min(min_sums, sums[i-k])
                    if sums[i] - min_sums >= 0:
                        ans = True
                        break
            return ans

        if not nums or len(nums) < k:
            return None

        left, right = min(nums), max(nums)
        while right - left > 1e-6:
            mid = (left + right) / 2.0
            if check(mid):
                left = mid
            else:
                right = mid
        return right

    # Follow up 1: length between k1 and k2
    # sliding windows minimum
    def maxAverage1(self, nums, k1, k2):
        def check(x):
            print x
            q, n = deque(), len(nums)
            ans, sums = False, [0]
            for i in xrange(1, n+1):
                sums.append(sums[i-1] + nums[i-1] - x)
                if i >= k1:
                    while len(q) > 0 and q[-1] > sums[i-k1]:
                        q.pop()
                    q.append(sums[i-k1])
                    if i > k2 and q[0] == sums[i-k2]:
                        q.popleft()
                    if sums[i] - q[0] >= 0:
                        ans = True
                        break
            return ans

        if not nums or len(nums) < k1:
            return None

        left, right = min(nums), max(nums)
        while right - left > 1e-6:
            mid = (left + right) / 2.0
            if check(mid):
                left = mid
            else:
                right = mid
        return right

if __name__ == '__main__':
    s = Solution()
    print s.maxAverage1([1, 12, -5, -6, 50, 3], 3, 5), '#', '15.667'
    print s.maxAverage([1, 12, -5, -6, 50, 3], 3), '#', '15.667'
