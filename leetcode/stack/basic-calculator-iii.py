# https://leetcode.com/problems/basic-calculator-iii/

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        total = num = prev = 0
        sign, s = '+', s + '+'
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c in '+-*/':
                total, prev = self.eval(sign, total, prev, num)
                sign, num = c, 0
            elif c == '(':
                stack.append((total, prev, sign))
                total, prev, sign = 0, 0, '+'
            elif c == ')':
                num, _ = self.eval(sign, total, prev, num)
                total, prev, sign = stack.pop()
        return total
                
    def eval(self, sign, total, prev, num):
        if sign == '+':
            prev = num
            total += num
        elif sign == '-':
            prev = -num
            total -= num
        elif sign == '*':
            total -= prev
            prev *= num
            total += prev
        elif sign == '/':
            total -= prev
            prev = int(1.0 * prev / num)
            total += prev
        return total, prev
