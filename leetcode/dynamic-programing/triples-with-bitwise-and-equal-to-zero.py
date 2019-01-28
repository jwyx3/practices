# https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/
# https://www.acwing.com/solution/leetcode/content/876/
# memorized iteration
# Time: O(N**2 + N*M), N is length of A and M is max(A)
# Space: O(M)
# the number of unique A[i]&A[j] is small!

class Solution(object):
    def countTriplets(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        res = 0
        f = [-1 for _ in xrange(1 << 16)]
        for i in xrange(N):
            for j in xrange(N):
                x = A[i] & A[j]
                if f[x] == -1:
                    f[x] = 0
                    for k in xrange(N):
                        if x & A[k] == 0:
                            f[x] += 1
                res += f[x]
        return res

# dp
# Time: O(M*N), M is max(A)
# Space: O(M)
# slower!

class Solution(object):
    def countTriplets(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # dp(i, s): number of solution with indices i and state s
        # dp(i, s&A[j]) += dp(i-1, s)
        # initial: for each j, dp(0, A[j]) += 1
        # answer: dp(2, 0)
        
        N = len(A)
        res = 0
        dp = [[0] * (1 << 16) for _ in xrange(3)]
        for j in xrange(N):
            dp[0][A[j]] += 1
        for i in xrange(1, 3):
            for s in xrange(1 << 16):
                if dp[i-1][s]:
                    for j in xrange(N):
                        dp[i][s&A[j]] += dp[i-1][s]
        return dp[2][0]
