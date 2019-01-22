# https://leetcode.com/problems/prison-cells-after-n-days/
# https://leetcode.com/problems/prison-cells-after-n-days/solution/
# https://leetcode.com/problems/prison-cells-after-n-days/discuss/205684/JavaPython-Find-the-Loop-or-Mod-14
# K is the number of cells
# Time: O(2**K*K)
# Space: O(2**K*K)

class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        def ncells():
            return [int(0 < i < 7 and cells[i-1] == cells[i+1]) for i, _ in enumerate(cells)]
        
        visited = {}
        while N > 0:
            k = tuple(cells)
            if k in visited:
                # visited[k] - N: cycle
                N %= visited[k] - N
            visited[k] = N
            # remember last cells
            if N >= 1:
                cells = ncells()
            N -= 1
        return cells
