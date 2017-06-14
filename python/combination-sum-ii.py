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

class Solution:
    """
    @param candidates: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    # diff: each number in candidates may only be used once!!
    def combinationSum2(self, candidates, target):
        ans = []
        if not candidates or target <= 0:
            return ans
        candidates.sort()
        self.dfs(candidates, target, [], ans)
        return ans

    def dfs(self, candidates, target, combination, ans):
        if target <= 0:
            if target == 0:
                ans.append(combination[:])
            return
        for i, num in enumerate(candidates):
            # remove duplicate
            if i > 0 and candidates[i - 1] == candidates[i]:
                continue
            combination.append(num)
            # use once for each element; only diff with combination-sum
            self.dfs(candidates[i+1:], target - num, combination, ans)
            combination.pop()
