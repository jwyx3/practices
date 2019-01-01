# https://leetcode.com/problems/is-graph-bipartite/
# node in A and another node in B
# we don't care if one node doesn't have edge


class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        N = len(graph)
        color = [-1] * N
        # for all components
        for start in xrange(N):
            if graph[start] and color[start] < 0:
                # bfs
                q = collections.deque([start])
                color[start] = 0
                while q:
                    node = q.popleft()
                    for nei in graph[node]:
                        if color[nei] < 0:
                            color[nei] = 1 ^ color[node]
                            q.append(nei)
                        elif color[nei] == color[node]:
                            return False
        return True

