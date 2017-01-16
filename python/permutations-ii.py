class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    def permuteUnique(self, nums):
        # write your code here
        def dfs(nums, permutation, visited, result):
            if len(nums) == len(permutation):
                result.append(permutation[:])
                return
            for i in xrange(len(nums)):
                # if element i hasn't been used or
                # the element i can only be used when i - 1 is be used when nums[i] == nums[i-1]
                if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
                    continue
                visited[i] = True
                permutation.append(nums[i])
                dfs(nums, permutation, visited, result)
                permutation.pop()
                visited[i] = False
        result = []
        # must sort and initialize visited
        dfs(sorted(nums), [], dict.fromkeys(xrange(len(nums)), False), result)
        return result
