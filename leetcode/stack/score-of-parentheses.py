# https://leetcode.com/problems/score-of-parentheses
# https://leetcode.com/problems/score-of-parentheses/solution/
# Time: O(N)
# Space: O(N)

class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        # use stack, need to know what we should calculate for each level
        # what the relationship between elements within same levels: A + B
        stack = [0]  # answer so far in this level
        for c in S:
            if c == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)
        return stack[0]

# Space: O(1)
# from solution
# The final sum will be a sum of powers of 2,
# as every core (a substring (), with score 1) will have it's score multiplied by 2 for each exterior set of parentheses that contains that core.
class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        # find '()' and its weight
        res = 0
        balance = 0
        for i, c in enumerate(S):
            if c == '(':
                balance += 1
            else:
                balance -= 1
                if i > 0 and S[i-1] == '(':
                    res += 1 << balance
        return res
