# https://leetcode.com/problems/grid-illumination/
# Use hash-table + set
# Time: O(Q + L), L = len(lamps), Q = len(queries)
# Space: O(N + L)

class Solution(object):
    def gridIllumination(self, N, lamps, queries):
        """
        :type N: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # use dict instead of array. because 1 <= N <= 10^9
        rows = collections.Counter()
        cols = collections.Counter()
        up_down = collections.Counter()
        down_up = collections.Counter()
        lamps = set(map(tuple, lamps))
        
        def toggle(r, c, on):
            delta = 1 if on else -1
            rows[r] += delta
            cols[c] += delta
            up_down[r - c + N - 1] += delta
            down_up[r + c] += delta
            
        def query(r, c):
            if rows[r] or cols[c] or up_down[r - c + N - 1] or down_up[r + c]:
                return 1
            return 0
        
        for r, c in lamps:
            toggle(r, c, True)
        res = []
        for r, c in queries:
            res.append(query(r, c))
            for nr, nc in [
                    (r, c), (r+1, c), (r-1, c), (r, c+1), (r, c-1),
                    (r+1, c+1), (r+1, c-1), (r-1, c+1), (r-1, c-1)]:
                if 0 <= nr < N and 0 <= nc < N and (nr, nc) in lamps:
                    toggle(nr, nc, False)
                    lamps.discard((nr, nc))
        return res
