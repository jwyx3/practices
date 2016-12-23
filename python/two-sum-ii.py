class Solution:
    # @param nums, an array of integer
    # @param target, an integer
    # @return an integer
    def twoSum2(self, nums, target):
        nums = sorted(nums)
        size, count = len(nums), 0
        left, right = 0, size - 1
        while left < right:
            s = nums[left] + nums[right]
            if s > target:
                count += 1
                right -= 1
            else:
                left += 1
                # known count of left element
                count += (size - 1 - right)
        n = size - 1 - left - 1
        return reduce(lambda count, x: count + x + 1, range(n), count)

    # @param nums, an array of integer
    # @param target, an integer
    # @return an integer
    def twoSum2_1(self, nums, target):
        # NOTE: allow duplicate elements
        nums = sorted(nums)
        size, count = len(nums), 0
        left, right = 0, size - 1
        while left < right:
            s = nums[left] + nums[right]
            if s > target:
                count += (right - left)
                right -= 1
            else:
                left += 1
        return count

    # brute force!!
    def twoSum3(self, nums, target):
        nums = sorted(nums)
        size, count = len(nums), 0
        print nums, size, count
        i, j = 0, 0
        while i < size - 1:
            j = i + 1
            while j < size:
                if nums[i] + nums[j] > target:
                    count += 1
                else:
                    print nums[i], nums[j]
                j += 1
            i += 1
        return count

s = Solution()
print s.twoSum2([1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99], -64), 93
print s.twoSum2([2,7,11,15], 24), 1
