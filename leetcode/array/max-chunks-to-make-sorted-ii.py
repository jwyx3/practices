# https://leetcode.com/problems/max-chunks-to-make-sorted-ii/
# http://www.cnblogs.com/grandyang/p/8850299.html
# Time: O(NlogN)
# Space: O(N)
# use sum

class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        expected = sorted(arr)
        ans = sum1 = sum2 = 0
        for i in xrange(len(arr)):
            sum1 += arr[i]
            sum2 += expected[i]
            if sum1 == sum2:
                ans += 1
        return ans

# Time: O(N)
# Space: O(N)
# use max and min# 

class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        b = list(arr)  # backword
        for i in xrange(n - 2, -1, -1):
            b[i] = min(b[i], b[i + 1])
        ans, curr = 1, 0
        for i in xrange(n - 1):
            curr = max(curr, arr[i])
            if curr <= b[i+1]:
                ans += 1
        return ans
