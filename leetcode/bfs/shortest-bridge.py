# https://leetcode.com/problems/shortest-bridge/
# https://leetcode.com/problems/shortest-bridge/solution/
# We can use a depth-first search to find the islands, and a breadth-first search to "grow" one of them.
# dfs + bfs

class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        R, C = len(A), len(A[0])
        
        def neighbors(r, c):
            for nr, nc in ((r+1, c), (r-1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc
        
        def get_components():
            visited = set()
            components = []
            for r in xrange(R):
                for c in xrange(C):
                    v = A[r][c]
                    if v and (r ,c) not in visited:
                        stack = [(r, c)]
                        components.append(set(stack))
                        while stack:
                            node = stack.pop()
                            for nei in neighbors(*node):
                                if A[nei[0]][nei[1]] and nei not in components[-1]:
                                    components[-1].add(nei)
                                    stack.append(nei)
                        visited |= components[-1]
            return components

        src, dst = get_components()
        q = collections.deque([(s, 0) for s in src])
        visited = set(src)
        while q:
            node, d = q.popleft()
            if node in dst:
                return d - 1
            for nei in neighbors(*node):
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, d + 1))
        return 0
