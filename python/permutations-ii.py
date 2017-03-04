class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    def permuteUnique(self, nums):
        if nums is None:
            return []
        nums.sort()
        result = []
        self.dfs(nums, [], dict.fromkeys(range(len(nums)), 0), result)
        return result

    def dfs(self, nums, permutation, visited, result):
        if len(nums) == len(permutation):
            result.append(permutation[:])
            return
        for i, num in enumerate(nums):
            # if element i hasn't been used or
            # the element i can only be used when i - 1 is be used when nums[i] == nums[i-1]
            if i > 0 and nums[i - 1] == nums[i] and not visited[i - 1] or visited[i]:
                continue
            visited[i] = 1
            permutation.append(num)
            self.dfs(nums, permutation, visited, result)
            permutation.pop()
            visited[i] = 0

class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    # non-recursion
    def permuteUnique(self, nums):
        if nums is None:
            return []
        if len(nums) <= 1:
            return [nums]
        nums.sort()
        result = [nums[:]]
        while self.nextPermutation(nums):
            result.append(nums[:])
        return result

    # 1, 2, 3, 4, 5 => i = 3, j = 4
    # 1, 2, 3, 5, 4 => i = 2, j = 4
    # 1, 2, 4, 3, 5 => i = 3, j = 4
    # 1, 2, 4, 5, 3 => i = 2, j = 3
    # 1, 2, 5, 3, 4
    # ...
    def nextPermutation(self, nums):
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            self.reverse(nums, i + 1)
        return i >= 0

    def reverse(self, nums, start):
        left, right = start, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
