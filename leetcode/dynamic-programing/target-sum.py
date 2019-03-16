# https://leetcode.com/problems/target-sum/
# https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-494-target-sum/
# Time: O(M*N), M is sum(nums)
# Space: O(M*N)
# dp(i, j):how many ways to assign symbols for first i nums and target j
# dp(i + 1, j + nums[i]) += dp(i, j)
# dp(i + 1, j - nums[i]) += dp(i, j)
# initial: dp(0, 0) = 1
# answer: dp(n, S)
# range f i = [0, n], j = [-sum(nums), sum(nums)]

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return int(S == 0)
        n, m = len(nums), sum(nums)
        if S + m < 0 or S + m > 2*m:
            return 0
        dp = [[0] * (2*m + 1) for _ in xrange(n + 1)]
        dp[0][m] = 1
        for i in xrange(n):
            for j in xrange(2*m + 1):
                if dp[i][j]:
                    dp[i+1][j+nums[i]] += dp[i][j]
                    dp[i+1][j-nums[i]] += dp[i][j]
        return dp[n][S + m]

# reduce dimension

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return int(S == 0)
        n, m = len(nums), sum(nums)
        if S + m < 0 or S + m > 2*m:
            return 0
        dp = [[0] * (2*m + 1) for _ in xrange(2)]
        dp[0][m] = 1
        for i in xrange(n):
            for j in xrange(2*m + 1):
                if dp[i%2][j]:
                    dp[(i+1)%2][j+nums[i]] += dp[i%2][j]
                    dp[(i+1)%2][j-nums[i]] += dp[i%2][j]
                    dp[i%2][j] = 0
        return dp[n%2][S + m]

# use hash table
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return int(S == 0)
        n, m = len(nums), sum(nums)
        if S + m < 0 or S + m > 2*m:
            return 0
        dp = {m: 1}
        for i in xrange(n):
            new_dp = collections.Counter()
            for j in dp.iterkeys():
                new_dp[j+nums[i]] += dp[j]
                new_dp[j-nums[i]] += dp[j]
            dp = new_dp
        return dp[n][S + m]

# convert into 0-1 knapsack problem
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # divide into two subsets P and N
        # P: nums with postive sign
        # N: nums with negative sign
        # sum(P) - sum(N) = target 
        # -> 2*sum(P) = target + sum(N) + sum(P)
        # -> 2*sum(P) = target + sum(nums)
        # new problem: given nums, can we find subset which sum up to (target + sum(nums)) / 2
        # 0-1 knapsack problem
        if not nums:
            return int(S == 0)
        n, m = len(nums), sum(nums)
        if S > m or S < -m or (S + m) % 2:
            return 0
        target = (S + m) / 2
        dp = [0] * (m + 1)
        dp[0] = 1
        for i in xrange(n):
            for j in xrange(m - nums[i], -1, -1):
                dp[j + nums[i]] += dp[j]
        return dp[target]
