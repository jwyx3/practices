class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1

    # follow up 1
    # find the LAST index of max number < target
    def binarySearch1(self, nums, target):
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid - 1
        if nums[right] < target:
            return right
        if nums[left] < target:
            return left
        return -1

    # follow up 2
    # find the FIRST index of max number < target
    def binarySearch2(self, nums, target):
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid - 1
        if nums[right] < target:
            target = nums[right]
        elif nums[left] < target:
            target = nums[left]
        else:
            return -1

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] == target:
            return left
        return right

class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        return -1

if __name__ == '__main__':
    s = Solution()
    print s.binarySearch([1,4,4,5,7,7,8,9,9,10], 7), "#", "4"
    print s.binarySearch1([1,4,4,5,7,7,8,9,9,10], 5), "#", "2"
    print s.binarySearch2([1,4,4,5,7,7,8,9,9,10], 5), "#", "1"
