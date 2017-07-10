class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    # recursively, dfs, remove dup
    def subsetsWithDup(self, S):
        # write your code here
        def dfs(S, start_index, subset, result):
            result.append(subset[:])
            for i in xrange(start_index, len(S)):
                # keep first element for duplication
                # because all subsets starting from second duplicate element are duplicate
                if i > 0 and S[i] == S[i - 1] and i > start_index:
                    continue
                subset.append(S[i])
                dfs(S, i + 1, subset, result)
                subset.pop()
        result = []
        # must sort
        dfs(sorted(S), 0, [], result)
        return result

class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        def dfs(S, start_index, subset, ans):
            ans.append(subset[:])
            for i in range(start_index, len(S)):
                # skip subproblem with prefix subset + [S[i]]
                # because it's same as subproblem with prfix subset + [S[i-1]]
                if i > start_index and S[i - 1] == S[i]:
                    continue
                subset.append(S[i])
                dfs(S, i + 1, subset, ans)
                subset.pop()

        ans = []
        if S is None:
            return ans
        S.sort()
        dfs(S, 0, [], ans)
        return ans
