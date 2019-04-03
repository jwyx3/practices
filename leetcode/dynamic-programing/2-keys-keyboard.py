# https://leetcode.com/problems/2-keys-keyboard/
# http://www.cnblogs.com/grandyang/p/7439616.html
# recursion -> DP
# Time: O(n*n)
# Space: O(n)

class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[i]: min steps to get n 'A'. i=0...n
        # dp[i] = min{j + dp[i/j]}, if i % j == 0.
        # initial: dp[1] = 0, dp[i>1] = i
        # answer: dp[n]
        dp = [0] * (n + 1)
        for i in xrange(2, n + 1):
            dp[i] = i
            for j in xrange(i - 1, 1, -1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[i/j] + j)
        return dp[n]

# greedy
# https://leetcode.com/problems/2-keys-keyboard/solution/
# in the sequence of moves CPPCPPPPCP, the groups would be [CPP][CPPPP][CP].
# Time: O(sqrt(n))
# Space: O(1)

class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1: 0
        # 2: 2
        # 3: 3
        # 4: 4
        # 5: 5
        # 6: 5
        ans = 0
        # divide n in to prime factors
        # i + j <= i*j, i >= 2 and j >= 2
        for i in xrange(2, n + 1):
            while n % i == 0:
                ans += i
                n /= i
        return ans
