# https://leetcode.com/problems/super-egg-drop/
# https://www.acwing.com/solution/LeetCode/content/579/
# Time: O(KlogN)
# Space: O(K)
# state is different

class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        # dp(i, j): given i moves and j eggs, how many floor it can achieve
        # dp(i, j) = dp(i-1, j-1) + dp(i-1, j) + 1
        # initial: dp(*, 0) = 0, dp(1, k) = 1
        # answer: dp(m, K) >= N
        dp = [0] + [1] * K
        m = 1
        while dp[K] < N:
            for j in xrange(K, 0, -1):
                dp[j] = dp[j-1] + dp[j] + 1
            m += 1
        return m
