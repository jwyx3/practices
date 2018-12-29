# https://leetcode.com/problems/strobogrammatic-number-iii/

class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        self.res = 0
        self.tmpls = ('0%s0', '1%s1', '8%s8', '6%s9', '9%s6')
        self.helper(low, high, '')
        self.helper(low, high, '0')
        self.helper(low, high, '1')
        self.helper(low, high, '8')
        return self.res
        
    # bottom-up to generate each word
    def helper(self, low, high, w):
        nl, nh = len(low), len(high)
        if nl <= len(w) <= nh:
            # check '0'
            if nl == len(w) and w < low or nh == len(w) and w > high:
                return
            # don't count word starting with 0 if len(word) > 1
            # but it can be part of other word. E.g. 00 -> 1001
            if len(w) <= 1 or w[0] != '0':
                self.res += 1
        if len(w) + 2 > nh:
            return
        for tmpl in self.tmpls:
            self.helper(low, high, tmpl % w)

