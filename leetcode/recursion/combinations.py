# https://leetcode.com/problems/combinations/
# Time: O(2**(n-k)) ??
# Space: O(n)

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        
        # s is the start number to be process
        # curr is the current combination
        def dfs(s, curr):
            if len(curr) == k:
                ans.append(curr[:])
                return
            if s == n:
                return
            for i in xrange(s, n):
                if n - i + len(curr) < k:  # remaining + used < k
                    break
                curr.append(i + 1)
                dfs(i + 1, curr)
                curr.pop()
        
        dfs(0, [])
        return ans

# use divide and conquer

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return [[]]
        if n < k:
            return []
        nums1 = [x + [n] for x in self.combine(n - 1, k - 1)]
        nums2 = [x for x in self.combine(n - 1, k)]
        return nums1 + nums2

