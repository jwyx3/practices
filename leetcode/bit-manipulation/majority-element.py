class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 投票
        result = count = 0
        for num in nums:
            if count == 0: # 如果之前票数相同或者刚开始，重新选一个数
                result = num
                count = 1
            elif result == num: # 如果数相同，加1
                count += 1
            else: # 不同则减1
                count -= 1
        return result
