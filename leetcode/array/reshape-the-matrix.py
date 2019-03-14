# https://leetcode.com/problems/reshape-the-matrix/
# https://leetcode.com/problems/reshape-the-matrix/solution/
# Time: O(R*C)
# Space: O(R*C), answer

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not nums or not nums[0]:
            return nums
        R, C = len(nums), len(nums[0])
        if R*C != r*c:
            return nums
        idx = 0
        ans = [[0] * c for _ in xrange(r)]
        for i in xrange(R):
            for j in xrange(C):
                ans[idx / c][idx % c] = nums[i][j]
                idx += 1
        return ans
