class Solution:
    # @param A, a list of integers
    # @return a boolean

    # dp[i]: if you are able to reach the last index with i elements
    # dp[i] = (or dp[k]) for all k which A[k] + k >= i
    # initial: dp[0] = True
    # ans: dp[n-1]
    # LTE!
    def canJump(self, A):
        # write your code here
        if not A:
            return False
        dp = [False for i in xrange(len(A))]
        dp[0] = True
        for i in xrange(1, len(A)):
            for j in xrange(i):
                if dp[j] and j + A[j] >= i:
                    dp[i] = True
                    break
        return dp[len(A) - 1]

    # Greedy
    def canJump(self, A):
        if not A:
            return False
        farthest = A[0]
        for i in xrange(1, len(A)):
            # If i can be reached from beginning and
            # we can reach farther from i
            if i <= farthest and i + A[i] > farthest:
                farthest = A[i] + i
        return farthest >= len(A) - 1

