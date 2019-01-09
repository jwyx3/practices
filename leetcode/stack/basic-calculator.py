# https://leetcode.com/problems/basic-calculator/

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        operators = []
        operands = []
        num = i = 0
        while i < len(s):
            if s[i].isdigit():
                while i < len(s) and s[i].isdigit():
                    num = 10 * num + int(s[i])
                    i += 1
                if operands and operators and operators[-1] != '(':
                    op = operators.pop()
                    operands.append(operands.pop() + (1 if op == '+' else -1) * num)
                else:
                    operands.append(num)
                num = 0
                i -= 1
            elif s[i] in '(+-':
                operators.append(s[i])
            elif s[i] == ')':
                operators.pop()
                while len(operands) >= 2 and operators and operators[-1] != '(':
                    op = operators.pop()
                    num2, num1 = operands.pop(), operands.pop()
                    operands.append(num1 + (1 if op == '+' else -1) * num2)
            i += 1
        return operands[0]

# https://leetcode.com/problems/basic-calculator/discuss/62361/Iterative-Java-solution-with-stack
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res = num = 0
        sign, s = '+', s + '+' # sentinal
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c in '+-':
                res = self.eval(res, sign, num)
                sign, num = c, 0
            elif c == '(':
                stack.append((res, sign))
                res, sign = 0, '+'
            elif c == ')':
                num = self.eval(res, sign, num)
                res, sign = stack.pop()
        return res
    
    def eval(self, res, sign, num):
        res += (-1, 1)[sign == '+'] * num
        return res
