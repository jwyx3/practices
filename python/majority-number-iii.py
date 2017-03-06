class Solution:
    """
    @param nums: A list of integers
    @param k: As described
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        counter = dict.fromkeys(nums, 0)
        max_count, max_num = 0, -1
        for num in nums:
            counter[num] += 1
            if counter[num] > max_count:
                max_count = counter[num]
                max_num = num
        return max_num
