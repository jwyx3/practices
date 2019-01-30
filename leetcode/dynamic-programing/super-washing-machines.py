# https://leetcode.com/problems/super-washing-machines/
# https://www.acwing.com/solution/LeetCode/content/413/
# https://leetcode.com/problems/super-washing-machines/discuss/99187/Easy-understand-solution-O(n)-time-and-O(1)-space
# Time: O(N)
# Space: O(1)
# think each number as subproblem.

class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        # intuition: the machines with more dresses (>arg) need to choose left or right
        # because for each move, you could choose any m (1 ≤ m ≤ n) washing machines,
        # so one step is needed to move extra dresses (not related to distance).
        # left_sum: sum of A[:i]; right_sum = sum of A[i+1:]
        # to_left[i] = avg*i - left_sum
        # to_right[i] = avg*(n-1-i) - right_sum
        # max(to_left[i] + to_right[i])
        
        s, n = sum(machines), len(machines)
        avg, rem = divmod(s, n)
        if rem:
            return -1
        res = 0
        ls, rs = 0, s
        for i, num in enumerate(machines):
            rs -= num
            tl = max(avg * i - ls, 0)  # dresses to move left
            tr = max(avg * (n - 1 - i) - rs, 0)  # dresses to move left
            res = max(res, tl + tr)
            ls += num
        return res
