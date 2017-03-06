class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """

    # pick up two numbers, drop them if they are different
    # the majority number are left numbers
    def majorityNumber(self, nums):
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count += 1
            elif candidate == num:
                count += 1
            else:
                count -= 1
        return candidate

