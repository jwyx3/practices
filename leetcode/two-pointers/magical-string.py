# https://leetcode.com/problems/magical-string/
# Time: O(N)
# Space: O(N)

class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n <= 3:
            return 1
        # start from 122, value is based on nums[j] while count is based on nums[i]
        nums = collections.deque([2])
        ans, k = 1, 3
        while k < n:
            new_num = nums[-1] ^ 3
            count = nums.popleft()
            nums.extend([new_num] * count)
            k += count
            if new_num == 1:
                ans += count
                if k > n:
                    ans -= k - n
        return ans
