# https://leetcode.com/problems/freedom-trail/
# http://www.cnblogs.com/grandyang/p/6675879.html
# Time: O(N*M**2)
# Space: O(M)

class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        # n = len(key), m = len(ring)
        # dp(i,j): min steps to spell key[i-1:] ending at ring[j]
        # dp(i,j) = min(dp(i,j), dp(i+1,k) + step)
        # step = min(diff, m-diff), diff = abs(j-k), if ring[k] == key[i] and ring[j] == key[i-1]
        # initial: dp(n, *) = 0, otherwise sys.maxint
        # answer: dp(0, 0) + n
        m, n = len(ring), len(key)
        dp = [[0] * m for _ in xrange(2)]
        for i in xrange(n - 1, -1, -1):
            for j in xrange(m):
                dp[i%2][j] = sys.maxint
                # i == 0 used to calculate result
                # ring[j] == key[i-1] only care about valid case
                if i == 0 or ring[j] == key[i-1]:
                    for k in xrange(m):
                        if ring[k] == key[i]:
                            diff = abs(j - k)
                            step = min(diff, m - diff)
                            dp[i%2][j] = min(dp[i%2][j], dp[(i + 1)%2][k] + step)
        return dp[0][0] + n  # consider press button cases
