# https://leetcode.com/problems/minimum-cost-to-merge-stones/
# https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-1000-minimum-cost-to-merge-stones/
# https://leetcode.com/problems/minimum-cost-to-merge-stones/discuss/247700/O(n3)-C%2B%2B-Bottom-Up-DP
# Time: O((N**3) / K)
# Space: O(N**2)

class Solution(object):
    def mergeStones(self, stones, K):
        """
        :type stones: List[int]
        :type K: int
        :rtype: int
        """
        # dp[l][i]: min cost to merge `consecutive` stones[i:i+l] into as less piles as possible
        # dp[l][i] = min(dp[m][i] + dp[l-m][i+m]), 1<=m<l
        # initial: dp[1][*] = 0, otherwise inf
        # answer: dp[n][0]
        n = len(stones)
        if (n - 1) % (K - 1) != 0:
            return -1
        dp = [[float('inf')] * n for _ in xrange(n + 1)]
        for l in xrange(K):
            for i in xrange(n):
                dp[l][i] = 0  # no merge cost for <K elements
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + stones[i]
        for l in xrange(K, n + 1):
            for i in xrange(n - l + 1):
                # m = 1, no merge. m = K, one merge. ..
                for m in xrange(1, l, K - 1):
                    dp[l][i] = min(dp[l][i], dp[m][i] + dp[l-m][i+m])
                # last merge.
                if (l - 1) % (K - 1) == 0:
                    dp[l][i] += sums[i+l] - sums[i]
        return dp[n][0]
