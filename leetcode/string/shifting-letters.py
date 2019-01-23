# https://leetcode.com/problems/shifting-letters/
# https://leetcode.com/problems/shifting-letters/solution/
# Time: O(N)
# Space: O(N)
# use prefix sum

class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        # prefix sums from back to front, we can calculate sum first
        res = []
        s = sum(shifts) % 26
        for i, c in enumerate(S):
            start = ord(c) - ord('a')
            res.append(chr(ord('a') + (start + s) % 26))
            s -= shifts[i]
        return ''.join(res)
