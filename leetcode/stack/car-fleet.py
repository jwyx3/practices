# https://leetcode.com/problems/car-fleet/
# Time: O(NlogN)
# Space: O(N)

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        N = len(position)
        stack = []
        cars = zip(position, speed)
        cars.sort()
        for pos, s in cars:
            t = float(target - pos) / s  # s is speed, t is time to reach target
            while stack and stack[-1] <= t:  # descending stack
                stack.pop()
            stack.append(t)
        return len(stack)
