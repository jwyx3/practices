class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win

    # dp[i]: the max number current player can get when there are i stones
    # sums[i]: the total number of i stones
    # dp[i] = max(sums[i] - dp[i-1], sums[i] - dp[i-2])
    # initial: dp[1] = A[1], dp[2] = A[1] + A[2]
    # ans: dp[n] > sums[n]/2
    def firstWillWin(self, values):
        A, n = values, len(values)
        if n == 0:
            return False
        if n <= 2:
            return True
        # pick from left, so reverse it
        A.reverse()
        sums = [0, A[0], A[0] + A[1]]
        dp = [0, sums[1], sums[2]]
        for i in range(3, n + 1):
            sums[i % 3] = sums[(i - 1) % 3] + A[i - 1]
            # sums[i] - dp[i-1]: if current player pick one, the value he can get
            dp[i % 3] = max(sums[i % 3] - dp[(i - 1) % 3], sums[i % 3] - dp[(i - 2) % 3])
        return dp[n % 3] > (sums[n % 3] / 2)

if __name__ == '__main__':
    s = Solution()
    print s.firstWillWin([1,2,4]), '#', 'false'
    print s.firstWillWin([1,2,2]), '#', 'true'
