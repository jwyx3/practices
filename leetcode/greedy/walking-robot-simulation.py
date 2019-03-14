# https://leetcode.com/problems/walking-robot-simulation/
# Time: O(N)
# Space: O(N)

class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        obstacles = set(tuple(x) for x in obstacles)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        x = y = 0
        ans = 0
        for cmd in commands:
            if cmd >= 1:
                dx, dy = dirs[d]
                for _ in xrange(cmd):
                    if (x + dx, y + dy) in obstacles:
                        break
                    x, y = dx + x, dy + y
                    ans = max(ans, x*x + y*y)
            elif cmd == -1:
                d = (d + 1) % 4
            else:
                d = (d - 1) % 4
        return ans
