# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of graph nodes in topological order.
    """
    def topSort(self, graph):
        counter = dict.fromkeys(graph, 0)

        for i in graph:
            for j in i.neighbors:
                counter[j] += 1

        ans = []
        for i in graph:
            if counter[i] == 0:
                self.dfs(i, counter, ans)
        return ans

    def dfs(self, i, counter, ans):
        ans.append(i)
        counter[i] -= 1
        for j in i.neighbors:
            counter[j] -= 1
            if counter[j] == 0:
                self.dfs(j, counter, ans)
