class Solution:
    # @param {int[]} nums an array of integers
    # @return {int} the number of unique integers

    # O(n):
    def deduplication(self, nums):
        if not nums:
            return 0
        visited, curt = {}, 0
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            visited[nums[i]] = 1
            nums[curt] = nums[i]
            curt += 1
        return curt

    # O(nlogn)
    def deduplication1(self, nums):
        if not nums:
            return 0
        nums.sort()
        curt = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            nums[curt] = nums[curt]
            curt += 1
        return curt
