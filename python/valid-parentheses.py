class Solution:
    # @param {string} s A string
    # @return {boolean} whether the string is a valid parentheses

    def isValidParentheses(self, s):
        stack, d = [], {'(': ')', '{': '}', '[': ']'}
        for p in s:
            if p in d:
                stack.append(p)
            else:
                if stack and d[stack[-1]] == p:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
