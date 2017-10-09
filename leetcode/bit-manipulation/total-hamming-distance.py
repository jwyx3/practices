# idea: 每一个0和1的个数相乘之后的和

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, mask = 0, 1
        for i in range(32):
            count1 = 0
            for num in nums:
                if num & mask:
                    count1 += 1
            # 每一位0和1的个数相乘
            mask <<= 1
            result += count1 * (len(nums) - count1)
        return result
