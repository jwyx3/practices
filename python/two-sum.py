class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    # time O(nlogn), space O(n): two pointers
    def twoSum(self, numbers, target):
        if not numbers or len(numbers) <= 1:
            return [-1, -1]
        nums = [(num, idx) for idx, num in enumerate(numbers)]
        nums.sort(key=lambda x: x[0])
        left, right = 0, len(nums) - 1
        while left < right:
            left_val, left_idx = nums[left]
            right_val, right_idx = nums[right]
            if left_val + right_val == target:
                return sorted([left_idx + 1, right_idx + 1])
            elif left_val + right_val < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]

    # time O(n), space O(n): hash
    def twoSum0(self, numbers, target):
        if not numbers or len(numbers) <= 1:
            return [-1, -1]
        visited = {}
        for idx, num in enumerate(numbers):
            rest = target - num
            if rest in visited:
                return [visited[rest] + 1, idx + 1]
            visited[num] = idx
        return [-1, -1]
