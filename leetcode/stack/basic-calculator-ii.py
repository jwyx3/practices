# https://leetcode.com/problems/basic-calculator-ii/

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        res = prev = num = 0
        sign, s = '+', s + '+'        
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in '+-/*':
                # use sign instead of c because the operand of c is not ready
                res, prev = self.eval(res, prev, sign, num)
                num, sign = 0, c
        return res
    
    def eval(self, res, prev, sign, num):
        if sign == '+':
            prev = num
            res += num
        elif sign == '-':
            prev = -num
            res -= num
        elif sign == '*':
            res -= prev
            prev *= num
            res += prev
        elif sign == '/':
            res -= prev
            prev = int(1.0 * prev / num)
            res += prev
        return res, prev
