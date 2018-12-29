# https://leetcode.com/problems/strobogrammatic-number-ii/
#
# tips
# 1) define problem as smaller problem
# 
# n = 2
# - 2 2 (?)
#     - 0 2 ([''])
#   2 2 (['11', '88', '69', '96']) # backtracking

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.tmpls = ('1%s1', '8%s8', '6%s9', '9%s6')
        return self.helper(n, n)
        
    def helper(self, n, m):
        if n == 0: return ['']
        if n == 1: return ['0', '1', '8']
        
        res = []
        nums = self.helper(n - 2, m)
        for num in nums:
            # don't use 0 as prefix
            if n != m:
                res.append('0%s0' % num)
            for tmpl in self.tmpls:
                res.append(tmpl % num)
        return res
