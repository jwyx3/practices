# https://leetcode.com/problems/valid-permutations-for-di-sequence/
# https://leetcode.com/problems/valid-permutations-for-di-sequence/discuss/168278/C%2B%2BJavaPython-DP-Solution-O(N2)
# Time: O(N**3)
# Space: O(N**2)

class Solution(object):
    def numPermsDISequence(self, S):
        """
        :type S: str
        :rtype: int
        """
        # dp(i, j): the number of valid permutation for first i + 1 elements
        #           which last element is (j + 1)th element within remaining choices
        n = len(S)
        dp = [[0] * (n + 1) for _ in xrange(n + 1)]
        # from 0..n, choose one element and last element is (j+1)th element within n+1 choices
        # the number permutation is 1
        for j in xrange(n + 1):
            dp[0][j] = 1
        for i in xrange(1, n + 1):
            c = S[i - 1]
            m = n + 1 - i  # choices
            for j in xrange(m):
                if c == 'D':
                    # preview choice is m + 1, preview last element should be [j+1, m] th
                    dp[i][j] = sum(dp[i-1][k] for k in xrange(j + 1, m + 1))
                else:
                    # preview last element can be [0, j], beccause the original j+1 th become j th in this round
                    dp[i][j] = sum(dp[i-1][k] for k in xrange(j + 1))
        return dp[n][0] % (10**9 + 7)

# optimization, using rolling array and prefix sum
# Time: O(N**2)
# Space: O(N)
