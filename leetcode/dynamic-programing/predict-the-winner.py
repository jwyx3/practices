# https://leetcode.com/problems/predict-the-winner/
# Time: O(N**2)
# Space: O(N**2)

class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # dp(i, j): the max scores for current player with scores [i, j]
        # dp(i, j) = max(nums[i] + s(i+1, j) - dp(i+1, j),
        #                nums[j] + s(i, j-1) - dp(i, j-1))
        #          = max(s(i, j) - dp(i+1, j), s(i, j) - dp(i, j-1))
        # s(i, j) = psums(j + 1) - psums(i)
        # initial: dp(i, i) = nums[i]
        # answer: dp(0, n-1) >= s(0, n-1)/2
        if not nums or len(nums) <= 2:
            return True
        n = len(nums)
        dp = [[0] * n for _ in xrange(n)]
        for i in xrange(n):
            dp[i][i] = nums[i]
        psums = [0]
        for num in nums:
            psums.append(psums[-1] + num)
        for k in xrange(2, n + 1):
            for i in xrange(n - k + 1):
                j = i + k - 1
                s = psums[j+1] - psums[i]
                dp[i][j] = max(s - dp[i+1][j], s - dp[i][j-1])
        return dp[0][n-1] >= psums[-1] / 2.0

# reduce space
# https://leetcode.com/problems/predict-the-winner/solution/
# Space: O(N)

class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) <= 2:
            return True
        n = len(nums)
        dp = [0] * n
        psums = [0]
        for num in nums:
            psums.append(psums[-1] + num)
        for i in xrange(n - 1, -1, -1):
            for j in xrange(i, n):
                if i == j:
                    dp[j] = nums[i]
                else:
                    s = psums[j+1] - psums[i]
                    dp[j] = max(s - dp[j], s - dp[j-1])
        return dp[n-1] >= psums[-1] / 2.0
