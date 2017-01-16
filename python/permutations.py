class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    # recursively, dfs
    def permute(self, nums):
        # write your code here
        def dfs(nums, permutation, result):
            if len(permutation) == len(nums):
                result.append(permutation[:])
                return
            for x in nums:
                if x in permutation:
                    continue
                permutation.append(x)
                dfs(nums, permutation, result)
                permutation.pop()
        result = []
        dfs(nums, [], result)
        return result

