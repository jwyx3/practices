class Solution:
    # @param nums, an array of integer
    # @param target, an integer
    # @return an integer
    def twoSum2(self, nums, target):
        if not nums or len(nums) < 2:
            return 0
        nums.sort()
        count, left, right = 0, 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] > target:
                count += (right - left)
                right -= 1
            else:
                left += 1
        return count

    # TODO: 用平衡树或线段数

if __name__ == '__main__':
    s = Solution()
    print s.twoSum2([1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99], -64), 93
    print s.twoSum2([2,7,11,15], 24), 1
