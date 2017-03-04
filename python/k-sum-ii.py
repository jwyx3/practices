class Solution:
    """
    @param A: An integer array.
    @param k: A positive integer (k <= length(A))
    @param target: Integer
    @return a list of lists of integer
    """
    def kSumII(self, A, k, target):
        if not A or k <= 0:
            return []
        result = []
        self.dfs(A, k, target, len(A) - 1, [], result)
        return result

    def dfs(self, A, k, target, index, nums, result):
        if k == 0 and target == 0:
            result.append(nums[:])
            return
        if k < 0 or target < 0 or index < 0:
            return
        self.dfs(A, k, target, index - 1, nums, result)
        nums.append(A[index])
        self.dfs(A, k - 1, target - A[index], index - 1, nums, result)
        nums.pop()
