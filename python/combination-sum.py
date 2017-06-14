class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        ans = []
        if not candidates or target <= 0:
            return ans
        # sort!! used for removing duplicate
        candidates.sort()
        self.dfs(candidates, target, [], ans)
        return ans

    # traversal
    def dfs(self, candidates, target, combination, ans):
        if target <= 0:
            if target == 0:
                # copy combination
                ans.append(combination[:])
            return

        for i, num in enumerate(candidates):
            # remove duplicate
            if i > 0 and candidates[i - 1] == candidates[i]:
                continue
            combination.append(num)
            self.dfs(candidates[i:], target - num, combination, ans)
            combination.pop()
