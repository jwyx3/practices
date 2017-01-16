class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    # recursively, dfs
    def subsets(self, S):
        # definition: get all subsets using subset as prefix
        def dfs(S, start_index, subset, result):
            result.append(subset[:])
            for i in xrange(start_index, len(S)):
                subset.append(S[i])
                dfs(S, i + 1, subset, result)
                subset.pop()

        result = []
        dfs(sorted(S), 0, [], result)
        return result

    # bfs
    def subsets(self, S):
        result = [[]]
        for x in sorted(S):
            result.extend([subset + [x] for subset in result])
        return result
