class Solution:
    # @param {int} n an integer
    # @return {int} an integer

    # NOTE: remember solution!!
    def dropEggs(self, n):
        # Write your code here
        ans = 0
        while ans * (ans + 1) / 2 < n:
            ans += 1
        return ans

    def dropEggs(self, n):
        import math
        # the min integer meet: ans  * (ans + 1) / 2 >= n
        return int(math.ceil(math.sqrt(2 * n + 0.25) - 0.5))

    # another solution is DP which will also apply to dropEggs II
