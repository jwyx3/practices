# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


class ConnectedComponent(object):
    def __init__(self, x):
        self.label = x
        self.members = [x]


class Solution:
    # @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    # @return {int[][]} a connected set of a undirected graph
    def connectedSet(self, nodes):
        father = {}
        root_nodes = set()

        def add_node(a):
            if a not in father:
                father[a] = ConnectedComponent(a)
                root_nodes.add(a)

        def find(a):
            if father[a].label == a:
                return father[a]
            father[a] = find(father[a].label)
            return father[a]

        def union(a, b):
            ra = find(a)
            rb = find(b)
            if ra.label != rb.label:
                root_nodes.remove(ra.label)
                rb.members.extend(ra.members)
                father[ra.label] = rb

        for node in nodes:
            add_node(node.label)
            for neighbor in node.neighbors:
                add_node(neighbor.label)
                union(node.label, neighbor.label)

        ans = []
        for x in root_nodes:
            ans.append(sorted(father[x].members))
        return ans
