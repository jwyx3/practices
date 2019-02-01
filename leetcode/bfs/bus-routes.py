# https://leetcode.com/problems/bus-routes/
# https://leetcode.com/problems/bus-routes/solution/
# bfs using bus; otherwise MLE!
# corner case: S == T

class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0
        # use bus as node
        n = len(routes)
        routes = [set(route) for route in routes]
        graph = collections.defaultdict(set)
        for i, r1 in enumerate(routes):
            for j in xrange(i + 1, len(routes)):
                r2 = routes[j]
                if any(r in r2 for r in r1):
                    graph[i].add(j)
                    graph[j].add(i)
        targets = set()
        visited = set()
        for i, r in enumerate(routes):
            if S in r: 
                visited.add(i)
            if T in r: 
                targets.add(i)
        q = collections.deque(visited)
        res = 1
        while q:
            size = len(q)
            for _ in xrange(size):
                bus = q.popleft()
                if bus in targets:
                    return res
                for nei in graph[bus]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            res += 1
        return -1
