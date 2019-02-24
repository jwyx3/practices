# https://leetcode.com/problems/tallest-billboard/
# https://www.youtube.com/watch?v=WqLslW2sFxU
# Time: O(N*S), S = sum(rods)
# Space: O(S)
# Brute force: Time: O(3**N)

class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        # dp[i][d]: largest common height for two subsets with diff d with first i elements
        # assume h = rods[i-1]
        # 1.
        # dp[i][d] = dp[i-1][d], don't put x into any subset
        # 2. 
        # dp[i][d+h] = max(dp[i][d+h], dp[i-1][d]), put x into longer subset
        # 3.
        # put h into shorter subset. h >= d
        # dp[i][h-d] = max(dp[i][h-d], dp[i-1][d] + d)
        # put h in to shorter subset. h < d
        # dp[i][d-h] = max(dp[i][d-x], dp[i-1][d] + h)
        # combine two cases: dp[i][abs(h-d)] = max(dp[i][abs(h-d)], dp[i-1][d] + min(d, h))
        #
        # initial: dp[*][*] = -1, dp[0][0] = 0
        # answer: dp[N][0]
        N, S = len(rods), sum(rods)
        dp = [[-1] * (S + 1) for _ in xrange(2)]
        dp[0][0] = 0
        s = 0
        for i in xrange(1, N + 1):
            h = rods[i-1]
            # the range of d is the [0, sum(rods[:i-1])]
            for d in xrange(0, s + 1):
                if dp[(i-1)%2][d] < 0:
                    continue
                dp[i%2][d] = max(dp[i%2][d], dp[(i-1)%2][d])
                dp[i%2][d+h] = max(dp[i%2][d+h], dp[(i-1)%2][d])
                dp[i%2][abs(h-d)] = max(dp[i%2][abs(h-d)], dp[(i-1)%2][d] + min(d, h))
            s += h
        return dp[N%2][0]
