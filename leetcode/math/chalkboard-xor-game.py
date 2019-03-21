# https://leetcode.com/problems/chalkboard-xor-game/
# https://leetcode.com/problems/chalkboard-xor-game/discuss/121696/C%2B%2BJavaPython-3-lines-Easy-Solution-with-Complaint-and-Explanation
# Time: O(N)
# Space: O(1)

class Solution(object):
    def xorGame(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # https://docs.python.org/2/library/operator.html
        xor = reduce(operator.xor, nums)
        if xor == 0:
            return True
        # 1. len(nums) is even, because xor != 0.
        #    at least one element don't equal to xor
        #    Alice can remove this element.
        #    the remaining is not 0. Bob will remove the last one.
        #    so Alice win.
        # 2. len(nums) is odd, because xor != 0.
        #    Alice remove one element.
        #    If remaining == 0, Alice failed.
        #    Otherwise, Bob will have len(nums) - 1 is even and xor != 0.
        #    Bob will win.
        return len(nums) & 1 == 0
