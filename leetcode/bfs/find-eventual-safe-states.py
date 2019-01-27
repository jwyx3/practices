# https://leetcode.com/problems/find-eventual-safe-states/
# https://leetcode.com/problems/find-eventual-safe-states/solution/
# topological sort
# Time: O(N + E)
# Space: O(N)

class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        N = len(graph)
        safe = [0] * N
        
        # edge from i to j
        g = [set(x) for x in graph]  # outgoing
        rg = [set() for _ in xrange(N)]  # incomming
        
        q = collections.deque()
        for i, js in enumerate(g):
            if not js:
                q.append(i)
            for j in js:
                rg[j].add(i)

        while q:
            j = q.popleft()
            safe[j] = 1
            for i in rg[j]:
                g[i].discard(j)
                if not g[i]:
                    q.append(i)
        return [i for i in xrange(N) if safe[i]]

# dfs: can define as subproblem

class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        N = len(graph)
        # 0: not visited; 1: unsafe; 2: safe
        safe = [0] * N
        
        # given graph and i node, return whether i is safe
        def dfs(i):
            if safe[i]:
                return safe[i] == 2
            safe[i] = 1  # unsafe
            for j in graph[i]:
                if not dfs(j):
                    return False
            safe[i] = 2  # safe
            return True
        
        return [i for i in xrange(N) if dfs(i)]
