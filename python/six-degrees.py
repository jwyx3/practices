# Definition for Undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    '''
    @param {UndirectedGraphNode[]} graph a list of Undirected graph node
    @param {UndirectedGraphNode} s, t two Undirected graph nodes
    @return {int} an integer
    '''
    def sixDegrees(self, graph, s, t):
        # generate dict {x: [nodes]}
        # BFS from s with level, and if t is found return, check visited
        # return -1 if queue is empty
        import collections
        mapping = {}
        for node in graph:
            mapping[node] = node.neighbors
        q = collections.deque([s])
        visited = {s}
        distance = 0
        while q:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                if curr.label == t.label:
                    return distance
                for neighbor in mapping[curr]:
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)
            distance += 1
        return -1


