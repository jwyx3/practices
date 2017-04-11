# 解题思路
#
# 用三个指针start, mid, end
#
# start = mid = 0, end = len(nums) - 1
# start表示第一个可能不满足nums[start] < low的下标
# mid表示第一个可能不满足nums[mid] <= high的下标!!
# end表示第一个可能不满足nums[end] > high的下标
#
# 如果nums[mid] < low, 替换到start的位置并且start += 1;
# 因为所有小于mid的元素都nums[mid]<= high, 所以mid += 1
#
# 如果nums[mid] > high, 替换到end的位置并且end -= 1;
# 因为新的nums[mid]仍然可能不满足nums[mid] <= high, 所以保持mid不变
#
#如果满足low <= nums[mid] <= high, 所以mid += 1
#

class Solution:
    # @param {int[]} nums an integer array
    # @param {int} low an integer
    # @param {int} high an integer
    # @return nothing
    def partition2(self, nums, low, high):
        if not nums or low > high:
            return
        start, mid, end = 0, 0, len(nums) - 1
        while mid <= end:
            if nums[mid] < low:
                nums[start], nums[mid] = nums[mid], nums[start]
                start += 1
                mid += 1
            elif nums[mid] > high:
                nums[end], nums[mid] = nums[mid], nums[end]
                end -= 1
            else:
                mid += 1


if __name__ == '__main__':
    s = Solution()
    nums = [4,3,4,1,2,3,1,2]
    s.partition2(nums, 2, 3)
    print nums
