class Solution:
    # @param {int[]} stones a list of stones' positions in sorted ascending order
    # @return {boolean} true if the frog is able to cross the river or false


    # dp[i]: all possible k in stone i
    # dp[i] = set(k) which dp[j] + {k-1, k, k+1} == i, i is a stone
    # initial: dp[0] = set(0)
    # answer: len(dp[n]) > 0
    def canCross(self, stones):
        # Write your code here
        dp = {}
        for stone in stones:
            dp[stone] = set()
        dp[0].add(0)
        for stone in stones:
            for k in dp[stone]:
                if k - 1 > 0 and stone + k - 1 in dp:
                    dp[stone + k - 1].add(k - 1)
                if stone + k in dp:
                    dp[stone + k].add(k)
                if stone + k + 1 in dp:
                    dp[stone + k + 1].add(k + 1)
        return len(dp[stones[-1]]) > 0
