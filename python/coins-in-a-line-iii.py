class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win

    # dp[i][s]: the larger amount of money the current player can get with s coins start from i
    # sums[s]: the sum of first s coins
    # dp[i][s] = sums[i+s] - sums[i] - min(dp[i+1][s-1], dp[i][s-1])
    # initial: dp[i][1] = A[i]
    # ans: dp[0][n] > sums[n]/2
    # O(n^2)
    def firstWillWin(self, values):
        if not values or len(values) == 1:
            return True
        n, A = len(values), values
        sums = [0]
        for s in xrange(1, n+1):
            sums.append(sums[s-1] + A[s-1])
        dp = [[A[i] if s == 1 else 0 for s in xrange(n+1)] for i in xrange(n)]
        for s in xrange(2, n+1):
            for i in xrange(n-s+1):
                dp[i][s] = sums[i+s] - sums[i] - min(dp[i][s-1], dp[i+1][s-1])
        return dp[0][n] > sums[n]/2

    # TODO: 偶数的O(n)算法


if __name__ == '__main__':
    s = Solution()
    print s.firstWillWin([1,20,4]), "#", False
    print s.firstWillWin([1,2,3,4,5,6,7,8,13,11,10,9]), "#", True
