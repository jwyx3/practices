# https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        if not flights:
            return -1
        # graph
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # dijkstra
        dist = {}
        h = [(0, 0, src)]
        while h:
            d, k, node = heapq.heappop(h)
            if k > K + 1 or d > dist.get((node, k), float('inf')):
                continue
            if node == dst:
                return d
            dist[(node, k)] = d
            for nei, d2 in graph[node]:
                if d + d2 < dist.get((nei, k + 1), float('inf')):
                    heapq.heappush(h, (d + d2, k + 1, nei))
        return -1
