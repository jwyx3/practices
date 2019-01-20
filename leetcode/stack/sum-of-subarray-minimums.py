# https://leetcode.com/problems/sum-of-subarray-minimums/
# https://leetcode.com/problems/sum-of-subarray-minimums/solution/
# Time: O(N)
# Space: O(N)
# how does min(B) change if we add A[j]?
# RLE (run length encoding) of these critical points B

class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A: return 0
        stack = []
        res, dot = 0, 0
        for i, num in enumerate(A):
            count = 1
            while stack and stack[-1][0] >= num:
                x, c = stack.pop()
                dot -= x * c
                count += c
            stack.append((num, count))
            # sum of min(B) for subarray ending with A[i]
            dot += num * count
            res += dot
        # don't use 1e9 + 7 which will get float number
        return res % (10**9 + 7)
