# https://leetcode.com/problems/validate-stack-sequences/
# https://leetcode.com/problems/validate-stack-sequences/solution/
# simulate
# Time: O(N)
# Space: O(N)

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        N = len(popped)
        stack, j = [], 0
        for num in pushed:
            stack.append(num)
            while j < N and stack and popped[j] == stack[-1]:
                stack.pop()
                j += 1
        return not stack
