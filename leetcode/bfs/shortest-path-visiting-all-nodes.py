# https://leetcode.com/problems/shortest-path-visiting-all-nodes/
# https://leetcode.com/problems/shortest-path-visiting-all-nodes/solution/
# Time: O(2**N * N)??
# Space: O(2**N * N) 

class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        N = len(graph)
        q = collections.deque()
        dist = collections.defaultdict(lambda: N*N)
        for i in xrange(N):
            dist[1 << i, i] = 0
            q.append((1 << i, i))
        target = (1 << N) - 1
        while q:
            state, head = q.popleft()
            d = dist[state, head]
            if state == target:
                return d
            for nei in graph[head]:
                state2 = state | (1 << nei)
                if d + 1 < dist[state2, nei]:
                    dist[state2, nei] = d + 1
                    q.append((state2, nei))
        return -1
        
