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


