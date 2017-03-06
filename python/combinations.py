class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        if n < k or k < 0 or n < 1:
            return []
        result = []
        self.dfs(n, k, 1, [], result)
        return result

    # put all combinations prefixing with combination into result
    # find k numbers out of start ... n
    def dfs(self, n, k, start, combination, result):
        if k == 0:
            result.append(combination[:])
            return
        for i in range(start, n + 1 - k + 1):
            combination.append(i)
            self.dfs(n, k - 1, i + 1, combination, result)
            combination.pop()
