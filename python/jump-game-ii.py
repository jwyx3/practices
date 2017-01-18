class Solution:
    # @param A, a list of integers
    # @return an integer

    # dp[i]: min jumps to reach i
    # dp[i] = min(dp[k]) for all k which A[k] + k >= i
    # initial: dp[i] = 0
    # ans: dp[n-1]
    def jump(self, A):
        # write your code here
        if not A:
            return 0
        dp = [sys.maxint for i in xrange(len(A))]
        dp[0] = 0
        for i in xrange(1, len(A)):
            for j in xrange(i):
                if A[j] + j >= i and dp[j] + 1 < dp[i]:
                    dp[i] = dp[j] + 1
        return dp[len(A) - 1]

    # Greedy
    def jump(self, A):
        if not A:
            return 0
        start, end, ans = 0, 0, 0
        # If not reach end
        while end < len(A) - 1:
            ans += 1
            farthest = end
            # within reachable positions, get farthest
            for i in xrange(start, end + 1):
                if A[i] + i > farthest:
                    farthest = A[i] + i
            # get next reachable positions
            start = end + 1
            end = farthest
        return ans
