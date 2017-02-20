class Solution:
    # @param {int[]} nums an array of integers
    # @return {int} the number of unique integers

    # O(n)
    def deduplication(self, nums):
        if not nums:
            return 0
        visited, curt = {}, 0
        for num in nums:
            if num not in visited:
                visited[num] = 1
                nums[curt] = num
                curt += 1
        # curt point position after all unique elements
        return curt


    # O(nlogn) two pointers
    def deduplication(self, nums):
        if not nums:
            return 0
        nums.sort()

        curt = 0
        for i in xrange(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            nums[curt] = nums[i]
            curt += 1
        return curt
