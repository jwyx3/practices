# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

from collections import deque

class Solution:
    # @param {UndirectedGraphNode[]} graph a list of undirected graph node
    # @param {dict} values a dict, <UndirectedGraphNode, (int)value>
    # @param {UndirectedGraphNode} node an Undirected graph node
    # @param {int} target an integer
    # @return {UndirectedGraphNode} a node
    def searchNode(self, graph, values, node, target):
        if node is None or not graph:
            return None
        q = deque([node])
        # saved visited node
        visited = dict.fromkeys(graph, 0) # O(n)
        while len(q) > 0:
            curt = q.popleft() # O(1)
            visited[curt] = 1

            # always handle current node
            if values[curt] == target:
                return curt

            # prepare potential node
            for neighbor in curt.neighbors:
                # If not visited
                if visited[neighbor] == 0:
                    q.append(neighbor)  # O(1)
        return None

