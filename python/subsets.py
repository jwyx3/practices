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

    # non-recursion
    def subsets(self, S):
        result, n = [], len(S)
        S.sort()
        # each subset equal to one of 0 ~ 2^n - 1
        for i in range(1 << n):
            subset = []
            for j in range(n):
                if i & (1 << j):
                    subset.append(S[j])
            result.append(subset)
        return result
