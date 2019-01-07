# https://leetcode.com/problems/equal-rational-numbers/
# https://leetcode.com/problems/equal-rational-numbers/discuss/214203/C%2B%2BPython-Easy-Cheat

class Solution(object):
    def isRationalEqual(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def f(s):
            i = s.find('(')
            if i >= 0:
                res = s[:i] + s[i+1:-1] * 20
            else:
                res = s
            return float(res[:20])
        # error <= 1e11
        return f(S) == f(T)

# https://leetcode.com/problems/equal-rational-numbers/solution/
# TODO: add fraction method
