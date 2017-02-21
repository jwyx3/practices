class Solution:
    # @param {string} s  an expression includes numbers, letters and brackets
    # @return {string} a string
    def expressionExpand(self, s):
        # Write your code here
        if not s:
            return s
        stack, num = [], 0
        for c in s:
            if c.isalpha():
                stack.append(c)
            elif c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                stack.append(num)
                num = 0
            else:
                word = ''
                while len(stack) > 0:
                    top = stack.pop()
                    if isinstance(top, int):
                        word = word * top
                        stack.append(word)
                        break
                    word = top + word
        # If the final letter is not ], need to combine them
        return ''.join(stack)

