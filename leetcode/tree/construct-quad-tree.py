# https://leetcode.com/problems/construct-quad-tree/
# https://leetcode.com/problems/construct-quad-tree/discuss/151684/Recursive-Java-Solution
# Time: O(NlogN)
# Space: O(logN)

"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        if not grid or not grid[0]:
            return None
        
        def dfs(x1, x2, y1, y2):
            if x1 >= x2 or y1 >= y2:
                return None
            mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
            node = Node(grid[x1][y1], True, None, None, None, None)
            for x in xrange(x1, x2):
                for y in xrange(y1, y2):
                    if node.val != grid[x][y]:
                        node.isLeaf = False
                        break
            if not node.isLeaf:
                node.topLeft = dfs(x1, mid_x, y1, mid_y)
                node.topRight = dfs(x1, mid_x, mid_y, y2)
                node.bottomLeft = dfs(mid_x, x2, y1, mid_y)
                node.bottomRight = dfs(mid_x, x2, mid_y, y2)
            return node
        
        return dfs(0, len(grid), 0, len(grid[0]))
