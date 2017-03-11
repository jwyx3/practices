class Solution:
    # @param {string[]} tokens The Reverse Polish Notation
    # @return {int} the value
    def evalRPN(self, tokens):
        if not tokens:
            return 0
        stack = []
        for x in tokens:
            if x not in ['+', '-', '*', '/']:
                stack.append(int(x))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if x == '+':
                    stack.append(op1 + op2)
                elif x == '-':
                    stack.append(op1 - op2)
                elif x == '*':
                    stack.append(op1 * op2)
                else:
                    # -11 / 2 = -6
                    # int(-11.0 / 2) = -5
                    # 11 / 2 = 5
                    # int(11.0 / 2) = 5
                    stack.append(int(op1 * 1.0 / op2))
        return stack[0]
