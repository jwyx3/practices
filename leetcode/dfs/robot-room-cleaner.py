# https://leetcode.com/problems/robot-room-cleaner/
# dfs
# Time: O(M * N), process all nodes once
# Space: O(M * N), call stack and visited

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        # up, left, down, right
        delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        dir_index = {d: i for i, d in enumerate(delta)}
        
        def dfs(x, y, prev_dx, prev_dy):
            if (x, y) in visited:
                return
            visited.add((x, y))
            # start direction
            start = dir_index[(prev_dx, prev_dy)]
            for i in xrange(start, start + len(delta)):
                dx, dy = delta[i % len(delta)]
                robot.clean()
                if robot.move():
                    nx, ny = dx + x, dy + y
                    dfs(nx, ny, dx, dy)
                    # recover to original position and direction
                    robot.turnLeft()
                    robot.turnLeft()
                    robot.move()
                    robot.turnLeft()
                    robot.turnLeft()
                robot.turnLeft()
        # 0, 0 is relative source position used for de-dup
        dfs(0, 0, -1, 0)
                    
