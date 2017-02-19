class Solution:
    """
    @param candidates: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, candidates, target):
        ans = []
        if not candidates or target <= 0:
            return ans
        candidates.sort()
        self.dfs(candidates, target, 0, [], ans)
        return ans

    def dfs(self, candidates, target, start_index, combination, ans):
        if target <= 0:
            if target == 0:
                ans.append(combination[:])
            return

        for i, num in enumerate(candidates):
            if i < start_index:
                continue
            # [1, 0, ...] is duplicate with [0, 1, ...]
            # so remove [0, 1, ...]
            if i > start_index and candidates[i - 1] == candidates[i]:
                continue
            combination.append(num)
            self.dfs(candidates, target - num, i + 1, combination, ans)
            combination.pop()
