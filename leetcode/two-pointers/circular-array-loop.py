# https://leetcode.com/problems/circular-array-loop/
# https://blog.csdn.net/zjucor/article/details/79051695
# https://leetcode.com/problems/circular-array-loop/discuss/94148/Java-SlowFast-Pointer-Solution
# Time: O(N)
# Space: O(1)

class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # notice:
        # 1. A cycle must start and end at the same index and the cycle's length > 1.
        # 2. movements in a cycle must all follow a single direction.
        n = len(nums)
        
        def next(i):
            return (nums[i] + i) % n
        
        for i in xrange(n):
            if nums[i] == 0:
                continue
            slow, fast = i, next(i)
            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[next(fast)] > 0:
                if slow == fast:  # loop is detected
                    if slow == next(slow):  # one element in loop
                        break
                    return True
                slow = next(slow)
                fast = next(next(fast))
            # set visited pos
            j = i
            while nums[i] * nums[j] > 0:
                j0, j = j, next(j)
                nums[j0] = 0
        return False
