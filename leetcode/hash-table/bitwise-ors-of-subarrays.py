# https://leetcode.com/problems/bitwise-ors-of-subarrays/
# https://leetcode.com/problems/bitwise-ors-of-subarrays/discuss/165881/C%2B%2BJavaPython-O(30N)
# Time: O(NlogW), N is len(A), W is bits of A[0]
# Space: O(NlogW)

class Solution(object):
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = set()
        cur = {0}
        for a in A:
            cur = set((x | a) for x in cur) | {a}
            res |= cur
        return len(res)
