# https://leetcode.com/problems/number-of-music-playlists/
# https://leetcode.com/problems/number-of-music-playlists/discuss/178415/C%2B%2BJavaPython-DP-Solution
#
# dp[i][j]: number of list for i unique songs and j length playlist
# dp[i][j] = dp[i-1][j-1] * i # all songs should be listened once. the last song can be any of i
#          + dp[i][j-1] * (i - K)  # same song should be apart for K songs. the last song must be repeated song.
#                                  # must different from last K songs
# dp[i-1][j-1]: is one subproblem, and we have i such subproblems
# dp[i][j-1]: is collections of subproblems, for each one we have extended to (i - K) combinations
#
# initial: i == j, dp[i][j] = math.factorial(i), all songs should be played at least once.
#          i == k + 1, dp[i][*] = math.factorial(i), from one comment: the same songs must be K = N-1 songs apart, so the first N songs among L songs must be a permutation of N, so it's N!. Since the same songs must be at least K = N-1 songs apart again, the next N songs must repeat exact orders of the first N songs, ... In other words, the first N songs determine the whole list. Hope this helps.
# answer: dp[N][L] % mod
# Time: O(N*L)
# Space: O(N*L)

class Solution(object):
    def numMusicPlaylists(self, N, L, K):
        """
        :type N: int
        :type L: int
        :type K: int
        :rtype: int
        """
        dp = [[0] * (L + 1) for _ in xrange(N + 1)]
        for i in xrange(K + 1, N + 1):  # K < N <= L
            for j in xrange(i, L + 1):
                if i == j or i == K + 1:
                    dp[i][j] = math.factorial(i)
                else:
                    dp[i][j] = dp[i-1][j-1] * i + dp[i][j-1] * (i - K)
        return dp[N][L] % (10**9 + 7)

# space optimization: Space: O(L)
class Solution(object):
    def numMusicPlaylists(self, N, L, K):
        """
        :type N: int
        :type L: int
        :type K: int
        :rtype: int
        """
        dp = [[0] * (L + 1) for _ in xrange(2)]
        for i in xrange(K + 1, N + 1):  # K < N <= L
            for j in xrange(i, L + 1):
                if i == j or i == K + 1:
                    dp[i%2][j] = math.factorial(i)
                else:
                    dp[i%2][j] = dp[(i-1)%2][j-1] * i + dp[i%2][j-1] * (i - K)
        return dp[N%2][L] % (10**9 + 7)
