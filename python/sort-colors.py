class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    # use counting sort
    def sortColors(self, nums):
        if not nums:
            return
        # write your code here
        counter = dict.fromkeys(nums, 0)
        for num in nums:
            counter[num] += 1
        for i in xrange(len(nums)):
            for color in range(3):
                if counter[color] > 0:
                    nums[i] = color
                    counter[color] -= 1
                    break

    # use two pointer
    def sortColors(self, nums):
        if not nums:
            return

        left, mid, right = 0, 0, len(nums) - 1
        # because the left, mid and right are elements to be process
        # so we need to handle case of mid == right
        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 2:
                nums[right], nums[mid] = nums[mid], nums[right]
                right -= 1
            else:
                mid += 1

