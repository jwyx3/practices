# https://leetcode.com/problems/network-delay-time/
# one source node to all node
# weighted directed graph
# Time: O(E*logE)
# Space: O(N + E), N is amount of nodes, E is amount of edges.

class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        # Dijkstra's algorithm
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        dist = {}
        h = [(0, K)]
        while h:
            d, node = heapq.heappop(h)
            # this should be heapq issue. we add data for same node instead of update.
            # dijkstra gurantee that the first visited data has the smallest dist.
            # so we skip the rest of data for same node.
            if node in dist: 
                continue
            dist[node] = d
            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(h, (d2 + d, nei))
        return max(dist.values()) if len(dist) == N else -1
