class Solution:
    """
    @param candidates: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, candidates, target):
        if not candidates or target <= 0:
            return []
        result = []
        candidates.sort()
        self.dfs(candidates, 0, [], target, result)
        return result

    def dfs(self, candidates, start, combination, target, result):
        if target <= 0:
            if target == 0:
                result.append(combination[:])
            return
        for i, num in enumerate(candidates):
            # remove duplicate and select consective numbers for same value
            if i < start or i > start and candidates[i] == candidates[i - 1]:
                continue
            combination.append(num)
            self.dfs(candidates, i + 1, combination, target - num, result)
            combination.pop()
