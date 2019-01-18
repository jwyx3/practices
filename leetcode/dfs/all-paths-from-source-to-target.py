# DFS, a directed, acyclic graph
# Time: O(2**N * N * N); N nodes in one path, O(N) for each node, 2**N possible pathes
# Space: O(2**N * N); each path N, 2 ** N possible pathes


class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        return self.helper(graph, 0)
        
    def helper(self, graph, node):
        N = len(graph)
        if node == N - 1:
            return [[node]]
        res = []
        for nei in graph[node]:
            for path in self.helper(graph, nei):
                res.append([node] + path)  # O(N)
        return res
