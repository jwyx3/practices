# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    """
    @param graph: A list of Directed graph node
    @param s: the starting Directed graph node
    @param t: the terminal Directed graph node
    @return: a boolean value
    """

    # divide and conquer
    def hasRoute(self, graph, s, t):
        return self.dfs(graph, s, t, dict.fromkeys(graph, 0))

    def dfs(self, graph, s, t, visited):
        if visited[s]:
            return False
        if s == t:
            return True
        visited[s] = 1
        for neighbor in s.neighbors:
            if not visited[neighbor] and self.hasRoute(graph, neighbor, t):
                return True
        return False


# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
from collections import deque


class Solution:
    """
    @param graph: A list of Directed graph node
    @param s: the starting Directed graph node
    @param t: the terminal Directed graph node
    @return: a boolean value
    """
    def hasRoute(self, graph, s, t):
        if t == s:
            return True

        visited = dict.fromkeys(graph, 0)
        q = deque([s])
        visited[s] = 1
        while q:
            curt = q.popleft()
            for neighbor in curt.neighbors:
                if not visited[neighbor]:
                    q.append(neighbor)
                    visited[neighbor] = 1
                    if neighbor == t:
                        return True
        return False


