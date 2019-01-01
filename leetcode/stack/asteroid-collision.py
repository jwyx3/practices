# https://leetcode.com/problems/asteroid-collision/
# https://leetcode.com/problems/asteroid-collision/solution/

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        if not asteroids:
            return []
        stack = []
        for a in asteroids:
            # two cases for pop
            # if stack[-1] > -a: do nothing
            # if stack[-1] == -a: pop stack
            # if stack[-1] < -a: keep poping and then appending
            while stack and a < 0 < stack[-1]:
                if stack[-1] < -a:
                    stack.pop()
                    continue
                elif stack[-1] == -a:
                    stack.pop()
                break
            else:
                stack.append(a)
        return stack
