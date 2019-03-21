# https://leetcode.com/problems/find-permutation/
# https://leetcode.com/problems/find-permutation/discuss/96613/Java-O(n)-clean-solution-easy-to-understand
# Time: O(N)
# Space: O(1)

class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        if not s:
            return []
        
        i, ans = 0, [0] * (len(s) + 1)
        while i < len(s):
            if s[i] == 'I':
                ans[i] = i + 1
            else:
                j = i
                while i < len(s) and s[i] == 'D':
                    i += 1
                for k in xrange(j, i + 1):
                    ans[k] = i + j - k + 1
            i += 1
        # i may be len(s) or len(s) + 1
        # corner case: "I", "D", "DDIIDI"
        if i == len(s):
            ans[i] = i + 1
        return ans
