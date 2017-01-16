class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    # recursively, dfs
    def permute(self, nums):
        # write your code here
        def dfs(nums, permutation, visited, result):
            if len(permutation) == len(nums):
                result.append(permutation[:])
                return
            for x in nums:
                if visited[x]:
                    continue
                visited[x] = True
                permutation.append(x)
                dfs(nums, permutation, visited, result)
                permutation.pop()
                visited[x] = False
        result = []
        dfs(nums, [], dict.fromkeys(nums, False), result)
        return result

